"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypeRegistrationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.max_results
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.registration_status
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name


class ListTypeRegistrationsInput(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>"""
    registration_status_filter: NotRequired[
        "capo_cloudformation.types.registration_status.RegistrationStatus"
    ]
    """<p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>"""
    max_results: NotRequired["capo_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypeRegistrationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "type_name" in value:
        pairs.append((f"{prefix}.TypeName", str(value["type_name"])))
    if "type_arn" in value:
        pairs.append((f"{prefix}.TypeArn", str(value["type_arn"])))
    if "registration_status_filter" in value:
        import capo_cloudformation.types.registration_status

        capo_cloudformation.types.registration_status.serialize_query(
            value["registration_status_filter"],
            pairs,
            f"{prefix}.RegistrationStatusFilter",
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTypeRegistrationsInput:
    out: ListTypeRegistrationsInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_registration_status_filter = el.find("RegistrationStatusFilter")
    if child_registration_status_filter is not None:
        import capo_cloudformation.types.registration_status

        out["registration_status_filter"] = (
            capo_cloudformation.types.registration_status.deserialize_query(
                child_registration_status_filter
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
