"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTypesFromInstanceRequirementsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.virtualization_type_set


class GetInstanceTypesFromInstanceRequirementsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    architecture_types: NotRequired[
        "aws_sdk_ec2.types.architecture_type_set.ArchitectureTypeSet"
    ]
    """<p>The processor architecture type.</p>"""
    virtualization_types: NotRequired[
        "aws_sdk_ec2.types.virtualization_type_set.VirtualizationTypeSet"
    ]
    """<p>The virtualization type.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes required for the instance types.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceTypesFromInstanceRequirementsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "architecture_types" in value:
        import aws_sdk_ec2.types.architecture_type_set

        aws_sdk_ec2.types.architecture_type_set.serialize_ec2_query(
            value["architecture_types"], pairs, f"{prefix}.ArchitectureTypes"
        )
    if "virtualization_types" in value:
        import aws_sdk_ec2.types.virtualization_type_set

        aws_sdk_ec2.types.virtualization_type_set.serialize_ec2_query(
            value["virtualization_types"], pairs, f"{prefix}.VirtualizationTypes"
        )
    if "instance_requirements" in value:
        import aws_sdk_ec2.types.instance_requirements_request

        aws_sdk_ec2.types.instance_requirements_request.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{prefix}.InstanceRequirements"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "context" in value:
        pairs.append((f"{prefix}.Context", str(value["context"])))


def deserialize_ec2_query(
    el: Element,
) -> GetInstanceTypesFromInstanceRequirementsRequest:
    out: GetInstanceTypesFromInstanceRequirementsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ArchitectureTypes") is not None:
        import aws_sdk_ec2.types.architecture_type_set

        out["architecture_types"] = (
            aws_sdk_ec2.types.architecture_type_set.deserialize_ec2_query(
                el, "ArchitectureTypes"
            )
        )
    if el.find("VirtualizationTypes") is not None:
        import aws_sdk_ec2.types.virtualization_type_set

        out["virtualization_types"] = (
            aws_sdk_ec2.types.virtualization_type_set.deserialize_ec2_query(
                el, "VirtualizationTypes"
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import aws_sdk_ec2.types.instance_requirements_request

        out["instance_requirements"] = (
            aws_sdk_ec2.types.instance_requirements_request.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    return out
