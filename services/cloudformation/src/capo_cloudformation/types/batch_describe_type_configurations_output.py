"""Generated from Smithy shape ``com.amazonaws.cloudformation#BatchDescribeTypeConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.batch_describe_type_configurations_errors
    import capo_cloudformation.types.type_configuration_details_list
    import capo_cloudformation.types.unprocessed_type_configurations


class BatchDescribeTypeConfigurationsOutput(TypedDict, closed=True):
    errors: NotRequired[
        "capo_cloudformation.types.batch_describe_type_configurations_errors.BatchDescribeTypeConfigurationsErrors"
    ]
    """<p>A list of information concerning any errors generated during the setting of the specified configurations.</p>"""
    unprocessed_type_configurations: NotRequired[
        "capo_cloudformation.types.unprocessed_type_configurations.UnprocessedTypeConfigurations"
    ]
    """<p>A list of any of the specified extension configurations that CloudFormation could not process for any reason.</p>"""
    type_configurations: NotRequired[
        "capo_cloudformation.types.type_configuration_details_list.TypeConfigurationDetailsList"
    ]
    """<p>A list of any of the specified extension configurations from the CloudFormation registry.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDescribeTypeConfigurationsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "errors" in value:
        import capo_cloudformation.types.batch_describe_type_configurations_errors

        capo_cloudformation.types.batch_describe_type_configurations_errors.serialize_query(
            value["errors"], pairs, f"{prefix}.Errors"
        )
    if "unprocessed_type_configurations" in value:
        import capo_cloudformation.types.unprocessed_type_configurations

        capo_cloudformation.types.unprocessed_type_configurations.serialize_query(
            value["unprocessed_type_configurations"],
            pairs,
            f"{prefix}.UnprocessedTypeConfigurations",
        )
    if "type_configurations" in value:
        import capo_cloudformation.types.type_configuration_details_list

        capo_cloudformation.types.type_configuration_details_list.serialize_query(
            value["type_configurations"], pairs, f"{prefix}.TypeConfigurations"
        )


def deserialize_query(el: Element) -> BatchDescribeTypeConfigurationsOutput:
    out: BatchDescribeTypeConfigurationsOutput = {}  # type: ignore[typeddict-item]
    child_errors = el.find("Errors")
    if child_errors is not None:
        import capo_cloudformation.types.batch_describe_type_configurations_errors

        out["errors"] = (
            capo_cloudformation.types.batch_describe_type_configurations_errors.deserialize_query(
                child_errors
            )
        )
    child_unprocessed_type_configurations = el.find("UnprocessedTypeConfigurations")
    if child_unprocessed_type_configurations is not None:
        import capo_cloudformation.types.unprocessed_type_configurations

        out["unprocessed_type_configurations"] = (
            capo_cloudformation.types.unprocessed_type_configurations.deserialize_query(
                child_unprocessed_type_configurations
            )
        )
    child_type_configurations = el.find("TypeConfigurations")
    if child_type_configurations is not None:
        import capo_cloudformation.types.type_configuration_details_list

        out["type_configurations"] = (
            capo_cloudformation.types.type_configuration_details_list.deserialize_query(
                child_type_configurations
            )
        )
    return out
