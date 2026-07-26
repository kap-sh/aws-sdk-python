"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteGlobalTableWitnessGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.region_name


class DeleteGlobalTableWitnessGroupMemberAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The witness Region name to be removed from the MRSC global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteGlobalTableWitnessGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteGlobalTableWitnessGroupMemberAction:
    out: DeleteGlobalTableWitnessGroupMemberAction = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError(
            "DeleteGlobalTableWitnessGroupMemberAction.region_name required"
        )
    return out
