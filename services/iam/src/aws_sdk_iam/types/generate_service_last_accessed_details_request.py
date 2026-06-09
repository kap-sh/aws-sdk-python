"""Generated from Smithy shape ``com.amazonaws.iam#GenerateServiceLastAccessedDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.access_advisor_usage_granularity_type
    import aws_sdk_iam.types.arn_type


class GenerateServiceLastAccessedDetailsRequest(TypedDict):
    arn: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The ARN of the IAM resource (user, group, role, or managed policy) used to generate information about when the resource was last used in an attempt to access an Amazon Web Services service.</p>"""
    granularity: NotRequired[
        "aws_sdk_iam.types.access_advisor_usage_granularity_type.AccessAdvisorUsageGranularityType"
    ]
    """<p>The level of detail that you want to generate. You can specify whether you want to generate information about the last attempt to access services or actions. If you specify service-level granularity, this operation generates only service data. If you specify action-level granularity, it generates service and action data. If you don't include this optional parameter, the operation generates service data.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateServiceLastAccessedDetailsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "granularity" in value:
        import aws_sdk_iam.types.access_advisor_usage_granularity_type

        aws_sdk_iam.types.access_advisor_usage_granularity_type.serialize_query(
            value["granularity"], pairs, f"{prefix}.Granularity"
        )


def deserialize_query(el: Element) -> GenerateServiceLastAccessedDetailsRequest:
    out: GenerateServiceLastAccessedDetailsRequest = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError(
            "GenerateServiceLastAccessedDetailsRequest.arn required"
        )
    child_granularity = el.find("Granularity")
    if child_granularity is not None:
        import aws_sdk_iam.types.access_advisor_usage_granularity_type

        out["granularity"] = (
            aws_sdk_iam.types.access_advisor_usage_granularity_type.deserialize_query(
                child_granularity
            )
        )
    return out
