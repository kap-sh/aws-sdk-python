"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeRulesPackagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list
    import aws_sdk_inspector.types.locale


class DescribeRulesPackagesRequest(TypedDict):
    rules_package_arns: (
        "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the rules package that you want to describe.</p>"""
    locale: NotRequired["aws_sdk_inspector.types.locale.Locale"]
    """<p>The locale that you want to translate a rules package description into.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRulesPackagesRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["rulesPackageArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["rules_package_arns"]
        )
    )
    if "locale" in value:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRulesPackagesRequest:
    out: DescribeRulesPackagesRequest = {}  # type: ignore[typeddict-item]
    if "rulesPackageArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["rules_package_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRulesPackagesRequest.rules_package_arns required"
        )
    if "locale" in data:
        import aws_sdk_inspector.types.locale

        out["locale"] = aws_sdk_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
