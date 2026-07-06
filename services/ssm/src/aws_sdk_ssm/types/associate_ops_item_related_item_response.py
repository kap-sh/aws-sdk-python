"""Generated from Smithy shape ``com.amazonaws.ssm#AssociateOpsItemRelatedItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_related_item_association_id


class AssociateOpsItemRelatedItemResponse(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_ssm.types.ops_item_related_item_association_id.OpsItemRelatedItemAssociationId"
    ]
    """<p>The association ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateOpsItemRelatedItemResponse) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateOpsItemRelatedItemResponse:
    out: AssociateOpsItemRelatedItemResponse = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    return out
