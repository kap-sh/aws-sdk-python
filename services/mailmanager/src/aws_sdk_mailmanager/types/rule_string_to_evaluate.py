"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.analysis
    import aws_sdk_mailmanager.types.mime_header_attribute
    import aws_sdk_mailmanager.types.rule_client_certificate_attribute
    import aws_sdk_mailmanager.types.rule_string_email_attribute


class _RuleStringToEvaluate_Attribute(TypedDict):
    Attribute: (
        "aws_sdk_mailmanager.types.rule_string_email_attribute.RuleStringEmailAttribute"
    )


class _RuleStringToEvaluate_MimeHeaderAttribute(TypedDict):
    MimeHeaderAttribute: (
        "aws_sdk_mailmanager.types.mime_header_attribute.MimeHeaderAttribute"
    )


class _RuleStringToEvaluate_Analysis(TypedDict):
    Analysis: "aws_sdk_mailmanager.types.analysis.Analysis"


class _RuleStringToEvaluate_ClientCertificateAttribute(TypedDict):
    ClientCertificateAttribute: "aws_sdk_mailmanager.types.rule_client_certificate_attribute.RuleClientCertificateAttribute"


RuleStringToEvaluate: TypeAlias = (
    _RuleStringToEvaluate_Attribute
    | _RuleStringToEvaluate_MimeHeaderAttribute
    | _RuleStringToEvaluate_Analysis
    | _RuleStringToEvaluate_ClientCertificateAttribute
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.rule_string_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "MimeHeaderAttribute" in value:
        return {"MimeHeaderAttribute": value["MimeHeaderAttribute"]}
    elif "Analysis" in value:
        import aws_sdk_mailmanager.types.analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    elif "ClientCertificateAttribute" in value:
        import aws_sdk_mailmanager.types.rule_client_certificate_attribute

        return {
            "ClientCertificateAttribute": aws_sdk_mailmanager.types.rule_client_certificate_attribute.serialize_aws_json_1_0(
                value["ClientCertificateAttribute"]
            )
        }
    else:
        raise SerializationError("RuleStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleStringToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.rule_string_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.rule_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif "MimeHeaderAttribute" in data:
        return {"MimeHeaderAttribute": data["MimeHeaderAttribute"]}
    elif "Analysis" in data:
        import aws_sdk_mailmanager.types.analysis

        return {
            "Analysis": aws_sdk_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    elif "ClientCertificateAttribute" in data:
        import aws_sdk_mailmanager.types.rule_client_certificate_attribute

        return {
            "ClientCertificateAttribute": aws_sdk_mailmanager.types.rule_client_certificate_attribute.deserialize_aws_json_1_0(
                data["ClientCertificateAttribute"]
            )
        }
    else:
        raise DeserializationError("RuleStringToEvaluate: no recognized variant key")
