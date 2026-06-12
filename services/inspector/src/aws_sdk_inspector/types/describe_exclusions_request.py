"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeExclusionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_exclusions_arn_list
    import aws_sdk_inspector.types.locale


class DescribeExclusionsRequest(TypedDict):
    exclusion_arns: "aws_sdk_inspector.types.batch_describe_exclusions_arn_list.BatchDescribeExclusionsArnList"
    """<p>The list of ARNs that specify the exclusions that you want to describe.</p>"""
    locale: NotRequired["aws_sdk_inspector.types.locale.Locale"]
    """<p>The locale into which you want to translate the exclusion's title, description, and recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExclusionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_exclusions_arn_list

    out["exclusionArns"] = (
        aws_sdk_inspector.types.batch_describe_exclusions_arn_list.serialize_aws_json_1_1(
            value["exclusion_arns"]
        )
    )
    if "locale" in value:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExclusionsRequest:
    out: DescribeExclusionsRequest = {}  # type: ignore[typeddict-item]
    if "exclusionArns" in data:
        import aws_sdk_inspector.types.batch_describe_exclusions_arn_list

        out["exclusion_arns"] = (
            aws_sdk_inspector.types.batch_describe_exclusions_arn_list.deserialize_aws_json_1_1(
                data["exclusionArns"]
            )
        )
    else:
        raise DeserializationError("DescribeExclusionsRequest.exclusion_arns required")
    if "locale" in data:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
