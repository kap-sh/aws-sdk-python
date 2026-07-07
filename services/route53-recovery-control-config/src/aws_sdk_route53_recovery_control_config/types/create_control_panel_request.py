"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#CreateControlPanelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09


class CreateControlPanelRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>"""
    cluster_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster for the control panel.</p>"""
    control_panel_name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the control panel.</p>"""
    tags: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
    ]
    """<p>The tags associated with the control panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateControlPanelRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "control_panel_name" in value:
        out["ControlPanelName"] = value["control_panel_name"]
    if "tags" in value:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["Tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateControlPanelRequest:
    out: CreateControlPanelRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ControlPanelName" in data:
        out["control_panel_name"] = data["ControlPanelName"]
    if "Tags" in data:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.deserialize_json(
                data["Tags"]
            )
        )
    return out
