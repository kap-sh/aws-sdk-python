"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAccessScopeAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class StartNetworkInsightsAccessScopeAnalysisRequest(TypedDict):
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartNetworkInsightsAccessScopeAnalysisRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(
    el: Element,
) -> StartNetworkInsightsAccessScopeAnalysisRequest:
    out: StartNetworkInsightsAccessScopeAnalysisRequest = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
