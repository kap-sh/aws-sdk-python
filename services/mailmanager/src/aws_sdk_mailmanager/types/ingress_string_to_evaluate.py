"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_analysis
    import aws_sdk_mailmanager.types.ingress_string_email_attribute


class _IngressStringToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "aws_sdk_mailmanager.types.ingress_string_email_attribute.IngressStringEmailAttribute"


class _IngressStringToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "aws_sdk_mailmanager.types.ingress_analysis.IngressAnalysis"


IngressStringToEvaluate: TypeAlias = (
    _IngressStringToEvaluate_Attribute | _IngressStringToEvaluate_Analysis
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.ingress_string_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import aws_sdk_mailmanager.types.ingress_analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.ingress_analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    else:
        raise SerializationError("IngressStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressStringToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.ingress_string_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.ingress_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif "Analysis" in data:
        import aws_sdk_mailmanager.types.ingress_analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.ingress_analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    else:
        raise DeserializationError("IngressStringToEvaluate: no recognized variant key")
