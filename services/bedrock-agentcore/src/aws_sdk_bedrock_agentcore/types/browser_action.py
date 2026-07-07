"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.key_press_arguments
    import aws_sdk_bedrock_agentcore.types.key_shortcut_arguments
    import aws_sdk_bedrock_agentcore.types.key_type_arguments
    import aws_sdk_bedrock_agentcore.types.mouse_click_arguments
    import aws_sdk_bedrock_agentcore.types.mouse_drag_arguments
    import aws_sdk_bedrock_agentcore.types.mouse_move_arguments
    import aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments
    import aws_sdk_bedrock_agentcore.types.screenshot_arguments


class _BrowserAction_mouseClick(TypedDict, closed=True):
    mouseClick: (
        "aws_sdk_bedrock_agentcore.types.mouse_click_arguments.MouseClickArguments"
    )


class _BrowserAction_mouseMove(TypedDict, closed=True):
    mouseMove: "aws_sdk_bedrock_agentcore.types.mouse_move_arguments.MouseMoveArguments"


class _BrowserAction_mouseDrag(TypedDict, closed=True):
    mouseDrag: "aws_sdk_bedrock_agentcore.types.mouse_drag_arguments.MouseDragArguments"


class _BrowserAction_mouseScroll(TypedDict, closed=True):
    mouseScroll: (
        "aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments.MouseScrollArguments"
    )


class _BrowserAction_keyType(TypedDict, closed=True):
    keyType: "aws_sdk_bedrock_agentcore.types.key_type_arguments.KeyTypeArguments"


class _BrowserAction_keyPress(TypedDict, closed=True):
    keyPress: "aws_sdk_bedrock_agentcore.types.key_press_arguments.KeyPressArguments"


class _BrowserAction_keyShortcut(TypedDict, closed=True):
    keyShortcut: (
        "aws_sdk_bedrock_agentcore.types.key_shortcut_arguments.KeyShortcutArguments"
    )


class _BrowserAction_screenshot(TypedDict, closed=True):
    screenshot: (
        "aws_sdk_bedrock_agentcore.types.screenshot_arguments.ScreenshotArguments"
    )


BrowserAction: TypeAlias = (
    _BrowserAction_mouseClick
    | _BrowserAction_mouseMove
    | _BrowserAction_mouseDrag
    | _BrowserAction_mouseScroll
    | _BrowserAction_keyType
    | _BrowserAction_keyPress
    | _BrowserAction_keyShortcut
    | _BrowserAction_screenshot
)


# --- restJson1 ser/de ---
def serialize_json(value: BrowserAction) -> dict:
    if "mouseClick" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_click_arguments

        return {
            "mouseClick": aws_sdk_bedrock_agentcore.types.mouse_click_arguments.serialize_json(
                value["mouseClick"]
            )
        }
    elif "mouseMove" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_move_arguments

        return {
            "mouseMove": aws_sdk_bedrock_agentcore.types.mouse_move_arguments.serialize_json(
                value["mouseMove"]
            )
        }
    elif "mouseDrag" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_drag_arguments

        return {
            "mouseDrag": aws_sdk_bedrock_agentcore.types.mouse_drag_arguments.serialize_json(
                value["mouseDrag"]
            )
        }
    elif "mouseScroll" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments

        return {
            "mouseScroll": aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments.serialize_json(
                value["mouseScroll"]
            )
        }
    elif "keyType" in value:
        import aws_sdk_bedrock_agentcore.types.key_type_arguments

        return {
            "keyType": aws_sdk_bedrock_agentcore.types.key_type_arguments.serialize_json(
                value["keyType"]
            )
        }
    elif "keyPress" in value:
        import aws_sdk_bedrock_agentcore.types.key_press_arguments

        return {
            "keyPress": aws_sdk_bedrock_agentcore.types.key_press_arguments.serialize_json(
                value["keyPress"]
            )
        }
    elif "keyShortcut" in value:
        import aws_sdk_bedrock_agentcore.types.key_shortcut_arguments

        return {
            "keyShortcut": aws_sdk_bedrock_agentcore.types.key_shortcut_arguments.serialize_json(
                value["keyShortcut"]
            )
        }
    elif "screenshot" in value:
        import aws_sdk_bedrock_agentcore.types.screenshot_arguments

        return {
            "screenshot": aws_sdk_bedrock_agentcore.types.screenshot_arguments.serialize_json(
                value["screenshot"]
            )
        }
    else:
        raise SerializationError("BrowserAction: no variant present")


def deserialize_json(data: dict) -> BrowserAction:
    if "mouseClick" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_click_arguments

        return {
            "mouseClick": aws_sdk_bedrock_agentcore.types.mouse_click_arguments.deserialize_json(
                data["mouseClick"]
            )
        }
    elif "mouseMove" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_move_arguments

        return {
            "mouseMove": aws_sdk_bedrock_agentcore.types.mouse_move_arguments.deserialize_json(
                data["mouseMove"]
            )
        }
    elif "mouseDrag" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_drag_arguments

        return {
            "mouseDrag": aws_sdk_bedrock_agentcore.types.mouse_drag_arguments.deserialize_json(
                data["mouseDrag"]
            )
        }
    elif "mouseScroll" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments

        return {
            "mouseScroll": aws_sdk_bedrock_agentcore.types.mouse_scroll_arguments.deserialize_json(
                data["mouseScroll"]
            )
        }
    elif "keyType" in data:
        import aws_sdk_bedrock_agentcore.types.key_type_arguments

        return {
            "keyType": aws_sdk_bedrock_agentcore.types.key_type_arguments.deserialize_json(
                data["keyType"]
            )
        }
    elif "keyPress" in data:
        import aws_sdk_bedrock_agentcore.types.key_press_arguments

        return {
            "keyPress": aws_sdk_bedrock_agentcore.types.key_press_arguments.deserialize_json(
                data["keyPress"]
            )
        }
    elif "keyShortcut" in data:
        import aws_sdk_bedrock_agentcore.types.key_shortcut_arguments

        return {
            "keyShortcut": aws_sdk_bedrock_agentcore.types.key_shortcut_arguments.deserialize_json(
                data["keyShortcut"]
            )
        }
    elif "screenshot" in data:
        import aws_sdk_bedrock_agentcore.types.screenshot_arguments

        return {
            "screenshot": aws_sdk_bedrock_agentcore.types.screenshot_arguments.deserialize_json(
                data["screenshot"]
            )
        }
    else:
        raise DeserializationError("BrowserAction: no recognized variant key")
