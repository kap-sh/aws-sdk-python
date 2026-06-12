"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.domain_arn
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.domain_name
    import aws_sdk_sagemaker.types.domain_status
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.string1024


class DomainDetails(TypedDict):
    domain_arn: NotRequired["aws_sdk_sagemaker.types.domain_arn.DomainArn"]
    """<p>The domain's Amazon Resource Name (ARN).</p>"""
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    domain_name: NotRequired["aws_sdk_sagemaker.types.domain_name.DomainName"]
    """<p>The domain name.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.domain_status.DomainStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    url: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The domain's URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainDetails) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.domain_status

        out["Status"] = aws_sdk_sagemaker.types.domain_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainDetails:
    out: DomainDetails = {}  # type: ignore[typeddict-item]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.domain_status

        out["status"] = aws_sdk_sagemaker.types.domain_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Url" in data:
        out["url"] = data["Url"]
    return out
