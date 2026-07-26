"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListCheckDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.check_details
    import capo_wellarchitected.types.next_token


class ListCheckDetailsOutput(TypedDict, closed=True):
    check_details: NotRequired["capo_wellarchitected.types.check_details.CheckDetails"]
    """<p>The details about the Trusted Advisor checks related to the Well-Architected best practice.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCheckDetailsOutput) -> dict:
    out: dict = {}
    if "check_details" in value:
        import capo_wellarchitected.types.check_details

        out["CheckDetails"] = capo_wellarchitected.types.check_details.serialize_json(
            value["check_details"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCheckDetailsOutput:
    out: ListCheckDetailsOutput = {}  # type: ignore[typeddict-item]
    if "CheckDetails" in data:
        import capo_wellarchitected.types.check_details

        out["check_details"] = (
            capo_wellarchitected.types.check_details.deserialize_json(
                data["CheckDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
