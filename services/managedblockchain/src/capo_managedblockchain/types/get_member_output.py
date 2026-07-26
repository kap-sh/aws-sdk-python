"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetMemberOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.member


class GetMemberOutput(TypedDict, closed=True):
    member: NotRequired["capo_managedblockchain.types.member.Member"]
    """<p>The properties of a member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberOutput) -> dict:
    out: dict = {}
    if "member" in value:
        import capo_managedblockchain.types.member

        out["Member"] = capo_managedblockchain.types.member.serialize_json(
            value["member"]
        )
    return out


def deserialize_json(data: dict) -> GetMemberOutput:
    out: GetMemberOutput = {}  # type: ignore[typeddict-item]
    if "Member" in data:
        import capo_managedblockchain.types.member

        out["member"] = capo_managedblockchain.types.member.deserialize_json(
            data["Member"]
        )
    return out
