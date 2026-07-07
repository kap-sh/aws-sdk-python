"""Generated from Smithy shape ``com.amazonaws.acmpca#EdiPartyName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.string256


class EdiPartyName(TypedDict, closed=True):
    party_name: "aws_sdk_acm_pca.types.string256.String256"
    """<p>Specifies the party name.</p>"""
    name_assigner: NotRequired["aws_sdk_acm_pca.types.string256.String256"]
    """<p>Specifies the name assigner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdiPartyName) -> dict:
    out: dict = {}
    out["PartyName"] = value["party_name"]
    if "name_assigner" in value:
        out["NameAssigner"] = value["name_assigner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdiPartyName:
    out: EdiPartyName = {}  # type: ignore[typeddict-item]
    if "PartyName" in data:
        out["party_name"] = data["PartyName"]
    else:
        raise DeserializationError("EdiPartyName.party_name required")
    if "NameAssigner" in data:
        out["name_assigner"] = data["NameAssigner"]
    return out
