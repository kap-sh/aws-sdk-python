"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledBaselinesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baselines
    import aws_sdk_controltower.types.list_enabled_baselines_next_token


class ListEnabledBaselinesOutput(TypedDict):
    enabled_baselines: "aws_sdk_controltower.types.enabled_baselines.EnabledBaselines"
    """<p>Retuens a list of summaries of <code>EnabledBaseline</code> resources.</p>"""
    next_token: NotRequired[
        "aws_sdk_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
    ]
    """<p>A pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledBaselinesOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.enabled_baselines

    out["enabledBaselines"] = (
        aws_sdk_controltower.types.enabled_baselines.serialize_json(
            value["enabled_baselines"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnabledBaselinesOutput:
    out: ListEnabledBaselinesOutput = {}  # type: ignore[typeddict-item]
    if "enabledBaselines" in data:
        import aws_sdk_controltower.types.enabled_baselines

        out["enabled_baselines"] = (
            aws_sdk_controltower.types.enabled_baselines.deserialize_json(
                data["enabledBaselines"]
            )
        )
    else:
        raise DeserializationError(
            "ListEnabledBaselinesOutput.enabled_baselines required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
