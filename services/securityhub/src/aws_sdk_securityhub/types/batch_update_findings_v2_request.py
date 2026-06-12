"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.metadata_uid_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.ocsf_finding_identifier_list


class BatchUpdateFindingsV2Request(TypedDict):
    metadata_uids: NotRequired[
        "aws_sdk_securityhub.types.metadata_uid_list.MetadataUidList"
    ]
    """<p>The list of finding <code>metadata.uid</code> to indicate findings to update. Finding <code>metadata.uid</code> is a globally unique identifier associated with the finding. Customers cannot use <code>MetadataUids</code> together with <code>FindingIdentifiers</code>.</p>"""
    finding_identifiers: NotRequired[
        "aws_sdk_securityhub.types.ocsf_finding_identifier_list.OcsfFindingIdentifierList"
    ]
    """<p>Provides information to identify a specific V2 finding.</p>"""
    comment: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The updated value for a user provided comment about the finding. Minimum character length 1. Maximum character length 512.</p>"""
    severity_id: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The updated value for the normalized severity identifier. The severity ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 6, 99]. When customer provides the updated severity ID, the string sibling severity will automatically be updated in the finding.</p>"""
    status_id: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The updated value for the normalized status identifier. The status ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 99]. When customer provides the updated status ID, the string sibling status will automatically be updated in the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2Request) -> dict:
    out: dict = {}
    if "metadata_uids" in value:
        import aws_sdk_securityhub.types.metadata_uid_list

        out["MetadataUids"] = (
            aws_sdk_securityhub.types.metadata_uid_list.serialize_json(
                value["metadata_uids"]
            )
        )
    if "finding_identifiers" in value:
        import aws_sdk_securityhub.types.ocsf_finding_identifier_list

        out["FindingIdentifiers"] = (
            aws_sdk_securityhub.types.ocsf_finding_identifier_list.serialize_json(
                value["finding_identifiers"]
            )
        )
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "severity_id" in value:
        out["SeverityId"] = value["severity_id"]
    if "status_id" in value:
        out["StatusId"] = value["status_id"]
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsV2Request:
    out: BatchUpdateFindingsV2Request = {}  # type: ignore[typeddict-item]
    if "MetadataUids" in data:
        import aws_sdk_securityhub.types.metadata_uid_list

        out["metadata_uids"] = (
            aws_sdk_securityhub.types.metadata_uid_list.deserialize_json(
                data["MetadataUids"]
            )
        )
    if "FindingIdentifiers" in data:
        import aws_sdk_securityhub.types.ocsf_finding_identifier_list

        out["finding_identifiers"] = (
            aws_sdk_securityhub.types.ocsf_finding_identifier_list.deserialize_json(
                data["FindingIdentifiers"]
            )
        )
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "SeverityId" in data:
        out["severity_id"] = data["SeverityId"]
    if "StatusId" in data:
        out["status_id"] = data["StatusId"]
    return out
