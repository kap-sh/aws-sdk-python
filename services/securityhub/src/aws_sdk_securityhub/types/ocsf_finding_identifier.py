"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfFindingIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class OcsfFindingIdentifier(TypedDict):
    cloud_account_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Finding cloud.account.uid, which is a unique identifier in the Amazon Web Services account..</p>"""
    finding_info_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Finding finding_info.uid, which is a unique identifier for the finding from the finding provider.</p>"""
    metadata_product_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Finding metadata.product.uid, which is a unique identifier for the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OcsfFindingIdentifier) -> dict:
    out: dict = {}
    if "cloud_account_uid" in value:
        out["CloudAccountUid"] = value["cloud_account_uid"]
    if "finding_info_uid" in value:
        out["FindingInfoUid"] = value["finding_info_uid"]
    if "metadata_product_uid" in value:
        out["MetadataProductUid"] = value["metadata_product_uid"]
    return out


def deserialize_json(data: dict) -> OcsfFindingIdentifier:
    out: OcsfFindingIdentifier = {}  # type: ignore[typeddict-item]
    if "CloudAccountUid" in data:
        out["cloud_account_uid"] = data["CloudAccountUid"]
    if "FindingInfoUid" in data:
        out["finding_info_uid"] = data["FindingInfoUid"]
    if "MetadataProductUid" in data:
        out["metadata_product_uid"] = data["MetadataProductUid"]
    return out
