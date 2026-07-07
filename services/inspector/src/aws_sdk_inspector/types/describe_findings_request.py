"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list
    import aws_sdk_inspector.types.locale


class DescribeFindingsRequest(TypedDict, closed=True):
    finding_arns: "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    """<p>The ARN that specifies the finding that you want to describe.</p>"""
    locale: NotRequired["aws_sdk_inspector.types.locale.Locale"]
    """<p>The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFindingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["findingArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["finding_arns"]
        )
    )
    if "locale" in value:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFindingsRequest:
    out: DescribeFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["finding_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["findingArns"]
            )
        )
    else:
        raise DeserializationError("DescribeFindingsRequest.finding_arns required")
    if "locale" in data:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
