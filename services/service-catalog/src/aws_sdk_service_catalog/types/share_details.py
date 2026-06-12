"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.share_errors
    import aws_sdk_service_catalog.types.successful_shares


class ShareDetails(TypedDict):
    successful_shares: NotRequired[
        "aws_sdk_service_catalog.types.successful_shares.SuccessfulShares"
    ]
    """<p>List of accounts for whom the operation succeeded.</p>"""
    share_errors: NotRequired["aws_sdk_service_catalog.types.share_errors.ShareErrors"]
    """<p>List of errors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareDetails) -> dict:
    out: dict = {}
    if "successful_shares" in value:
        import aws_sdk_service_catalog.types.successful_shares

        out["SuccessfulShares"] = (
            aws_sdk_service_catalog.types.successful_shares.serialize_aws_json_1_1(
                value["successful_shares"]
            )
        )
    if "share_errors" in value:
        import aws_sdk_service_catalog.types.share_errors

        out["ShareErrors"] = (
            aws_sdk_service_catalog.types.share_errors.serialize_aws_json_1_1(
                value["share_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareDetails:
    out: ShareDetails = {}  # type: ignore[typeddict-item]
    if "SuccessfulShares" in data:
        import aws_sdk_service_catalog.types.successful_shares

        out["successful_shares"] = (
            aws_sdk_service_catalog.types.successful_shares.deserialize_aws_json_1_1(
                data["SuccessfulShares"]
            )
        )
    if "ShareErrors" in data:
        import aws_sdk_service_catalog.types.share_errors

        out["share_errors"] = (
            aws_sdk_service_catalog.types.share_errors.deserialize_aws_json_1_1(
                data["ShareErrors"]
            )
        )
    return out
