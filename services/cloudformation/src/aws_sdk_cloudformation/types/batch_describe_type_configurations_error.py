"""Generated from Smithy shape ``com.amazonaws.cloudformation#BatchDescribeTypeConfigurationsError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_code
    import aws_sdk_cloudformation.types.error_message
    import aws_sdk_cloudformation.types.type_configuration_identifier


class BatchDescribeTypeConfigurationsError(TypedDict):
    error_code: NotRequired["aws_sdk_cloudformation.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired[
        "aws_sdk_cloudformation.types.error_message.ErrorMessage"
    ]
    """<p>The error message.</p>"""
    type_configuration_identifier: NotRequired[
        "aws_sdk_cloudformation.types.type_configuration_identifier.TypeConfigurationIdentifier"
    ]
    """<p>Identifying information for the configuration of a CloudFormation extension.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDescribeTypeConfigurationsError,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "error_code" in value:
        pairs.append((f"{prefix}.ErrorCode", str(value["error_code"])))
    if "error_message" in value:
        pairs.append((f"{prefix}.ErrorMessage", str(value["error_message"])))
    if "type_configuration_identifier" in value:
        import aws_sdk_cloudformation.types.type_configuration_identifier

        aws_sdk_cloudformation.types.type_configuration_identifier.serialize_query(
            value["type_configuration_identifier"],
            pairs,
            f"{prefix}.TypeConfigurationIdentifier",
        )


def deserialize_query(el: Element) -> BatchDescribeTypeConfigurationsError:
    out: BatchDescribeTypeConfigurationsError = {}  # type: ignore[typeddict-item]
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        out["error_code"] = str(child_error_code.text or "")
    child_error_message = el.find("ErrorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    child_type_configuration_identifier = el.find("TypeConfigurationIdentifier")
    if child_type_configuration_identifier is not None:
        import aws_sdk_cloudformation.types.type_configuration_identifier

        out["type_configuration_identifier"] = (
            aws_sdk_cloudformation.types.type_configuration_identifier.deserialize_query(
                child_type_configuration_identifier
            )
        )
    return out
