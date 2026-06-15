"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserActionResult``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.key_press_result
    import aws_sdk_bedrock_agentcore.types.key_shortcut_result
    import aws_sdk_bedrock_agentcore.types.key_type_result
    import aws_sdk_bedrock_agentcore.types.mouse_click_result
    import aws_sdk_bedrock_agentcore.types.mouse_drag_result
    import aws_sdk_bedrock_agentcore.types.mouse_move_result
    import aws_sdk_bedrock_agentcore.types.mouse_scroll_result
    import aws_sdk_bedrock_agentcore.types.screenshot_result


class _BrowserActionResult_mouseClick(TypedDict):
    mouseClick: "aws_sdk_bedrock_agentcore.types.mouse_click_result.MouseClickResult"


class _BrowserActionResult_mouseMove(TypedDict):
    mouseMove: "aws_sdk_bedrock_agentcore.types.mouse_move_result.MouseMoveResult"


class _BrowserActionResult_mouseDrag(TypedDict):
    mouseDrag: "aws_sdk_bedrock_agentcore.types.mouse_drag_result.MouseDragResult"


class _BrowserActionResult_mouseScroll(TypedDict):
    mouseScroll: "aws_sdk_bedrock_agentcore.types.mouse_scroll_result.MouseScrollResult"


class _BrowserActionResult_keyType(TypedDict):
    keyType: "aws_sdk_bedrock_agentcore.types.key_type_result.KeyTypeResult"


class _BrowserActionResult_keyPress(TypedDict):
    keyPress: "aws_sdk_bedrock_agentcore.types.key_press_result.KeyPressResult"


class _BrowserActionResult_keyShortcut(TypedDict):
    keyShortcut: "aws_sdk_bedrock_agentcore.types.key_shortcut_result.KeyShortcutResult"


class _BrowserActionResult_screenshot(TypedDict):
    screenshot: "aws_sdk_bedrock_agentcore.types.screenshot_result.ScreenshotResult"


BrowserActionResult: TypeAlias = (
    _BrowserActionResult_mouseClick
    | _BrowserActionResult_mouseMove
    | _BrowserActionResult_mouseDrag
    | _BrowserActionResult_mouseScroll
    | _BrowserActionResult_keyType
    | _BrowserActionResult_keyPress
    | _BrowserActionResult_keyShortcut
    | _BrowserActionResult_screenshot
)


# --- restJson1 ser/de ---
def serialize_json(value: BrowserActionResult) -> dict:
    if "mouseClick" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_click_result

        return {
            "mouseClick": aws_sdk_bedrock_agentcore.types.mouse_click_result.serialize_json(
                value["mouseClick"]
            )
        }
    elif "mouseMove" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_move_result

        return {
            "mouseMove": aws_sdk_bedrock_agentcore.types.mouse_move_result.serialize_json(
                value["mouseMove"]
            )
        }
    elif "mouseDrag" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_drag_result

        return {
            "mouseDrag": aws_sdk_bedrock_agentcore.types.mouse_drag_result.serialize_json(
                value["mouseDrag"]
            )
        }
    elif "mouseScroll" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_scroll_result

        return {
            "mouseScroll": aws_sdk_bedrock_agentcore.types.mouse_scroll_result.serialize_json(
                value["mouseScroll"]
            )
        }
    elif "keyType" in value:
        import aws_sdk_bedrock_agentcore.types.key_type_result

        return {
            "keyType": aws_sdk_bedrock_agentcore.types.key_type_result.serialize_json(
                value["keyType"]
            )
        }
    elif "keyPress" in value:
        import aws_sdk_bedrock_agentcore.types.key_press_result

        return {
            "keyPress": aws_sdk_bedrock_agentcore.types.key_press_result.serialize_json(
                value["keyPress"]
            )
        }
    elif "keyShortcut" in value:
        import aws_sdk_bedrock_agentcore.types.key_shortcut_result

        return {
            "keyShortcut": aws_sdk_bedrock_agentcore.types.key_shortcut_result.serialize_json(
                value["keyShortcut"]
            )
        }
    elif "screenshot" in value:
        import aws_sdk_bedrock_agentcore.types.screenshot_result

        return {
            "screenshot": aws_sdk_bedrock_agentcore.types.screenshot_result.serialize_json(
                value["screenshot"]
            )
        }
    else:
        raise SerializationError("BrowserActionResult: no variant present")


def deserialize_json(data: dict) -> BrowserActionResult:
    if "mouseClick" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_click_result

        return {
            "mouseClick": aws_sdk_bedrock_agentcore.types.mouse_click_result.deserialize_json(
                data["mouseClick"]
            )
        }
    elif "mouseMove" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_move_result

        return {
            "mouseMove": aws_sdk_bedrock_agentcore.types.mouse_move_result.deserialize_json(
                data["mouseMove"]
            )
        }
    elif "mouseDrag" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_drag_result

        return {
            "mouseDrag": aws_sdk_bedrock_agentcore.types.mouse_drag_result.deserialize_json(
                data["mouseDrag"]
            )
        }
    elif "mouseScroll" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_scroll_result

        return {
            "mouseScroll": aws_sdk_bedrock_agentcore.types.mouse_scroll_result.deserialize_json(
                data["mouseScroll"]
            )
        }
    elif "keyType" in data:
        import aws_sdk_bedrock_agentcore.types.key_type_result

        return {
            "keyType": aws_sdk_bedrock_agentcore.types.key_type_result.deserialize_json(
                data["keyType"]
            )
        }
    elif "keyPress" in data:
        import aws_sdk_bedrock_agentcore.types.key_press_result

        return {
            "keyPress": aws_sdk_bedrock_agentcore.types.key_press_result.deserialize_json(
                data["keyPress"]
            )
        }
    elif "keyShortcut" in data:
        import aws_sdk_bedrock_agentcore.types.key_shortcut_result

        return {
            "keyShortcut": aws_sdk_bedrock_agentcore.types.key_shortcut_result.deserialize_json(
                data["keyShortcut"]
            )
        }
    elif "screenshot" in data:
        import aws_sdk_bedrock_agentcore.types.screenshot_result

        return {
            "screenshot": aws_sdk_bedrock_agentcore.types.screenshot_result.deserialize_json(
                data["screenshot"]
            )
        }
    else:
        raise DeserializationError("BrowserActionResult: no recognized variant key")
