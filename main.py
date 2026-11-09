from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

class MeanExtension(Extension):

    def __init__(self):
        super(MeanExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        word = event.get_argument()
        if not word:
            return RenderResultListAction([
                ExtensionResultItem(icon="dictionary-icon.png", name="Type a word", description="Example: mean serendipity", on_enter=HideWindowAction())])
        return RenderResultListAction([ExtensionResultItem(icon="dictionary-icon.png", name=f"You typed, {word}", description="Example: mean serendipity", on_enter=HideWindowAction())])

if __name__ == "__main__": 
    MeanExtension().run()