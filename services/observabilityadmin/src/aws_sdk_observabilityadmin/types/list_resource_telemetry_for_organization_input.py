"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListResourceTelemetryForOrganizationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.account_identifiers
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_max_results
    import aws_sdk_observabilityadmin.types.next_token
    import aws_sdk_observabilityadmin.types.resource_identifier_prefix
    import aws_sdk_observabilityadmin.types.resource_types
    import aws_sdk_observabilityadmin.types.tag_map_input
    import aws_sdk_observabilityadmin.types.telemetry_configuration_state


class ListResourceTelemetryForOrganizationInput(TypedDict):
    account_identifiers: NotRequired[
        "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
    ]
    """<p> A list of Amazon Web Services accounts used to filter the resources to those associated with the specified accounts. </p>"""
    resource_identifier_prefix: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
    ]
    """<p> A string used to filter resources in the organization which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>"""
    resource_types: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_types.ResourceTypes"
    ]
    """<p> A list of resource types used to filter resources in the organization. If this parameter is provided, the resources will be returned in the same order used in the request. </p>"""
    telemetry_configuration_state: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
    ]
    """<p> A key-value pair to filter resources in the organization based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
    ]
    r"""<p> A key-value pair to filter resources in the organization based on tags associated with the resource. Fore more information about tags, see <a href=\"https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html\">What are tags?</a> </p>"""
    max_results: NotRequired[
        "aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_max_results.ListResourceTelemetryForOrganizationMaxResults"
    ]
    """<p> A number field used to limit the number of results within the returned list. </p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p> The token for the next set of items to return. A previous call provides this token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTelemetryForOrganizationInput) -> dict:
    out: dict = {}
    if "account_identifiers" in value:
        import aws_sdk_observabilityadmin.types.account_identifiers

        out["AccountIdentifiers"] = (
            aws_sdk_observabilityadmin.types.account_identifiers.serialize_json(
                value["account_identifiers"]
            )
        )
    if "resource_identifier_prefix" in value:
        out["ResourceIdentifierPrefix"] = value["resource_identifier_prefix"]
    if "resource_types" in value:
        import aws_sdk_observabilityadmin.types.resource_types

        out["ResourceTypes"] = (
            aws_sdk_observabilityadmin.types.resource_types.serialize_json(
                value["resource_types"]
            )
        )
    if "telemetry_configuration_state" in value:
        import aws_sdk_observabilityadmin.types.telemetry_configuration_state

        out["TelemetryConfigurationState"] = (
            aws_sdk_observabilityadmin.types.telemetry_configuration_state.serialize_json(
                value["telemetry_configuration_state"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["ResourceTags"] = (
            aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
                value["resource_tags"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTelemetryForOrganizationInput:
    out: ListResourceTelemetryForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "AccountIdentifiers" in data:
        import aws_sdk_observabilityadmin.types.account_identifiers

        out["account_identifiers"] = (
            aws_sdk_observabilityadmin.types.account_identifiers.deserialize_json(
                data["AccountIdentifiers"]
            )
        )
    if "ResourceIdentifierPrefix" in data:
        out["resource_identifier_prefix"] = data["ResourceIdentifierPrefix"]
    if "ResourceTypes" in data:
        import aws_sdk_observabilityadmin.types.resource_types

        out["resource_types"] = (
            aws_sdk_observabilityadmin.types.resource_types.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if "TelemetryConfigurationState" in data:
        import aws_sdk_observabilityadmin.types.telemetry_configuration_state

        out["telemetry_configuration_state"] = (
            aws_sdk_observabilityadmin.types.telemetry_configuration_state.deserialize_json(
                data["TelemetryConfigurationState"]
            )
        )
    if "ResourceTags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["resource_tags"] = (
            aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
                data["ResourceTags"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
