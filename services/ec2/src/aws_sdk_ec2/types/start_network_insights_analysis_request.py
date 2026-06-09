"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.arn_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.value_string_list


class StartNetworkInsightsAnalysisRequest(TypedDict):
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
    additional_accounts: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The member accounts that contain resources that the path can traverse.</p>"""
    filter_in_arns: NotRequired["aws_sdk_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path must traverse.</p>"""
    filter_out_arns: NotRequired["aws_sdk_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path will ignore.</p>"""
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
    value: StartNetworkInsightsAnalysisRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_path_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInsightsPathId", str(value["network_insights_path_id"]))
        )
    if "additional_accounts" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["additional_accounts"], pairs, f"{prefix}.AdditionalAccounts"
        )
    if "filter_in_arns" in value:
        import aws_sdk_ec2.types.arn_list

        aws_sdk_ec2.types.arn_list.serialize_ec2_query(
            value["filter_in_arns"], pairs, f"{prefix}.FilterInArns"
        )
    if "filter_out_arns" in value:
        import aws_sdk_ec2.types.arn_list

        aws_sdk_ec2.types.arn_list.serialize_ec2_query(
            value["filter_out_arns"], pairs, f"{prefix}.FilterOutArns"
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


def deserialize_ec2_query(el: Element) -> StartNetworkInsightsAnalysisRequest:
    out: StartNetworkInsightsAnalysisRequest = {}  # type: ignore[typeddict-item]
    child_network_insights_path_id = el.find("NetworkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    if el.find("AdditionalAccounts") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["additional_accounts"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AdditionalAccounts"
            )
        )
    if el.find("FilterInArns") is not None:
        import aws_sdk_ec2.types.arn_list

        out["filter_in_arns"] = aws_sdk_ec2.types.arn_list.deserialize_ec2_query(
            el, "FilterInArns"
        )
    if el.find("FilterOutArns") is not None:
        import aws_sdk_ec2.types.arn_list

        out["filter_out_arns"] = aws_sdk_ec2.types.arn_list.deserialize_ec2_query(
            el, "FilterOutArns"
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
