"""Generated from Smithy shape ``com.amazonaws.dataexchange#ScopeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies
    import aws_sdk_dataexchange.types.list_of_redshift_data_shares
    import aws_sdk_dataexchange.types.list_of_s3_data_accesses


class ScopeDetails(TypedDict, closed=True):
    lake_formation_tag_policies: NotRequired[
        "aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies.ListOfLakeFormationTagPolicies"
    ]
    """<p>Underlying LF resources that will be affected by this notification.</p>"""
    redshift_data_shares: NotRequired[
        "aws_sdk_dataexchange.types.list_of_redshift_data_shares.ListOfRedshiftDataShares"
    ]
    """<p>Underlying Redshift resources that will be affected by this notification.</p>"""
    s3_data_accesses: NotRequired[
        "aws_sdk_dataexchange.types.list_of_s3_data_accesses.ListOfS3DataAccesses"
    ]
    """<p>Underlying S3 resources that will be affected by this notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeDetails) -> dict:
    out: dict = {}
    if "lake_formation_tag_policies" in value:
        import aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies

        out["LakeFormationTagPolicies"] = (
            aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies.serialize_json(
                value["lake_formation_tag_policies"]
            )
        )
    if "redshift_data_shares" in value:
        import aws_sdk_dataexchange.types.list_of_redshift_data_shares

        out["RedshiftDataShares"] = (
            aws_sdk_dataexchange.types.list_of_redshift_data_shares.serialize_json(
                value["redshift_data_shares"]
            )
        )
    if "s3_data_accesses" in value:
        import aws_sdk_dataexchange.types.list_of_s3_data_accesses

        out["S3DataAccesses"] = (
            aws_sdk_dataexchange.types.list_of_s3_data_accesses.serialize_json(
                value["s3_data_accesses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScopeDetails:
    out: ScopeDetails = {}  # type: ignore[typeddict-item]
    if "LakeFormationTagPolicies" in data:
        import aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies

        out["lake_formation_tag_policies"] = (
            aws_sdk_dataexchange.types.list_of_lake_formation_tag_policies.deserialize_json(
                data["LakeFormationTagPolicies"]
            )
        )
    if "RedshiftDataShares" in data:
        import aws_sdk_dataexchange.types.list_of_redshift_data_shares

        out["redshift_data_shares"] = (
            aws_sdk_dataexchange.types.list_of_redshift_data_shares.deserialize_json(
                data["RedshiftDataShares"]
            )
        )
    if "S3DataAccesses" in data:
        import aws_sdk_dataexchange.types.list_of_s3_data_accesses

        out["s3_data_accesses"] = (
            aws_sdk_dataexchange.types.list_of_s3_data_accesses.deserialize_json(
                data["S3DataAccesses"]
            )
        )
    return out
