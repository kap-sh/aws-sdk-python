"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledControlsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_controls


class ListEnabledControlsOutput(TypedDict, closed=True):
    enabled_controls: "aws_sdk_controltower.types.enabled_controls.EnabledControls"
    """<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains.</p>"""
    next_token: NotRequired["str"]
    """<p>Retrieves the next page of results. If the string is empty, the response is the end of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledControlsOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.enabled_controls

    out["enabledControls"] = aws_sdk_controltower.types.enabled_controls.serialize_json(
        value["enabled_controls"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnabledControlsOutput:
    out: ListEnabledControlsOutput = {}  # type: ignore[typeddict-item]
    if "enabledControls" in data:
        import aws_sdk_controltower.types.enabled_controls

        out["enabled_controls"] = (
            aws_sdk_controltower.types.enabled_controls.deserialize_json(
                data["enabledControls"]
            )
        )
    else:
        raise DeserializationError(
            "ListEnabledControlsOutput.enabled_controls required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
