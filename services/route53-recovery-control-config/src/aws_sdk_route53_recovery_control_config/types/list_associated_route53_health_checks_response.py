"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListAssociatedRoute53HealthChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max8096_pattern_s


class ListAssociatedRoute53HealthChecksResponse(TypedDict, closed=True):
    health_check_ids: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s.__listOf__stringMax36PatternS"
    ]
    """<p>Identifiers for the health checks.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max8096_pattern_s.__stringMin1Max8096PatternS"
    ]
    """<p>Next token for listing health checks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedRoute53HealthChecksResponse) -> dict:
    out: dict = {}
    if "health_check_ids" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s

        out["HealthCheckIds"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s.serialize_json(
                value["health_check_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedRoute53HealthChecksResponse:
    out: ListAssociatedRoute53HealthChecksResponse = {}  # type: ignore[typeddict-item]
    if "HealthCheckIds" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s

        out["health_check_ids"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_max36_pattern_s.deserialize_json(
                data["HealthCheckIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
