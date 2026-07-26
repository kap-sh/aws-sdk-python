"""Generated from Smithy shape ``com.amazonaws.datazone#AddPolicyGrantOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.grant_identifier


class AddPolicyGrantOutput(TypedDict, closed=True):
    grant_id: NotRequired["capo_datazone.types.grant_identifier.GrantIdentifier"]
    """<p>The ID of the policy grant that was added to a specified entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPolicyGrantOutput) -> dict:
    out: dict = {}
    if "grant_id" in value:
        out["grantId"] = value["grant_id"]
    return out


def deserialize_json(data: dict) -> AddPolicyGrantOutput:
    out: AddPolicyGrantOutput = {}  # type: ignore[typeddict-item]
    if "grantId" in data:
        out["grant_id"] = data["grantId"]
    return out
