"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListCheckDetailsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.check_details
    import aws_sdk_wellarchitected.types.next_token


class ListCheckDetailsOutput(TypedDict):
    check_details: NotRequired[
        "aws_sdk_wellarchitected.types.check_details.CheckDetails"
    ]
    """<p>The details about the Trusted Advisor checks related to the Well-Architected best practice.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCheckDetailsOutput) -> dict:
    out: dict = {}
    if "check_details" in value:
        import aws_sdk_wellarchitected.types.check_details

        out["CheckDetails"] = (
            aws_sdk_wellarchitected.types.check_details.serialize_json(
                value["check_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCheckDetailsOutput:
    out: ListCheckDetailsOutput = {}  # type: ignore[typeddict-item]
    if "CheckDetails" in data:
        import aws_sdk_wellarchitected.types.check_details

        out["check_details"] = (
            aws_sdk_wellarchitected.types.check_details.deserialize_json(
                data["CheckDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
