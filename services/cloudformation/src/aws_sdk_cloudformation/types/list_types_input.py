"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.deprecated_status
    import aws_sdk_cloudformation.types.max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.provisioning_type
    import aws_sdk_cloudformation.types.registry_type
    import aws_sdk_cloudformation.types.type_filters
    import aws_sdk_cloudformation.types.visibility


class ListTypesInput(TypedDict, closed=True):
    visibility: NotRequired["aws_sdk_cloudformation.types.visibility.Visibility"]
    """<p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and Region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and Region.</p> </li> <li> <p>Public extensions that you have activated in this account and Region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services and third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>"""
    provisioning_type: NotRequired[
        "aws_sdk_cloudformation.types.provisioning_type.ProvisioningType"
    ]
    """<p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>"""
    deprecated_status: NotRequired[
        "aws_sdk_cloudformation.types.deprecated_status.DeprecatedStatus"
    ]
    """<p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>"""
    type: NotRequired["aws_sdk_cloudformation.types.registry_type.RegistryType"]
    """<p>The type of extension.</p>"""
    filters: NotRequired["aws_sdk_cloudformation.types.type_filters.TypeFilters"]
    """<p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>"""
    max_results: NotRequired["aws_sdk_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "visibility" in value:
        import aws_sdk_cloudformation.types.visibility

        aws_sdk_cloudformation.types.visibility.serialize_query(
            value["visibility"], pairs, f"{prefix}.Visibility"
        )
    if "provisioning_type" in value:
        import aws_sdk_cloudformation.types.provisioning_type

        aws_sdk_cloudformation.types.provisioning_type.serialize_query(
            value["provisioning_type"], pairs, f"{prefix}.ProvisioningType"
        )
    if "deprecated_status" in value:
        import aws_sdk_cloudformation.types.deprecated_status

        aws_sdk_cloudformation.types.deprecated_status.serialize_query(
            value["deprecated_status"], pairs, f"{prefix}.DeprecatedStatus"
        )
    if "type" in value:
        import aws_sdk_cloudformation.types.registry_type

        aws_sdk_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "filters" in value:
        import aws_sdk_cloudformation.types.type_filters

        aws_sdk_cloudformation.types.type_filters.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTypesInput:
    out: ListTypesInput = {}  # type: ignore[typeddict-item]
    child_visibility = el.find("Visibility")
    if child_visibility is not None:
        import aws_sdk_cloudformation.types.visibility

        out["visibility"] = aws_sdk_cloudformation.types.visibility.deserialize_query(
            child_visibility
        )
    child_provisioning_type = el.find("ProvisioningType")
    if child_provisioning_type is not None:
        import aws_sdk_cloudformation.types.provisioning_type

        out["provisioning_type"] = (
            aws_sdk_cloudformation.types.provisioning_type.deserialize_query(
                child_provisioning_type
            )
        )
    child_deprecated_status = el.find("DeprecatedStatus")
    if child_deprecated_status is not None:
        import aws_sdk_cloudformation.types.deprecated_status

        out["deprecated_status"] = (
            aws_sdk_cloudformation.types.deprecated_status.deserialize_query(
                child_deprecated_status
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_cloudformation.types.registry_type

        out["type"] = aws_sdk_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_cloudformation.types.type_filters

        out["filters"] = aws_sdk_cloudformation.types.type_filters.deserialize_query(
            child_filters
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
