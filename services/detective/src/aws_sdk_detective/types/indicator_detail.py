"""Generated from Smithy shape ``com.amazonaws.detective#IndicatorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.flagged_ip_address_detail
    import aws_sdk_detective.types.impossible_travel_detail
    import aws_sdk_detective.types.new_aso_detail
    import aws_sdk_detective.types.new_geolocation_detail
    import aws_sdk_detective.types.new_user_agent_detail
    import aws_sdk_detective.types.related_finding_detail
    import aws_sdk_detective.types.related_finding_group_detail
    import aws_sdk_detective.types.tt_ps_observed_detail


class IndicatorDetail(TypedDict):
    tt_ps_observed_detail: NotRequired[
        "aws_sdk_detective.types.tt_ps_observed_detail.TTPsObservedDetail"
    ]
    """<p>Details about the indicator of compromise.</p>"""
    impossible_travel_detail: NotRequired[
        "aws_sdk_detective.types.impossible_travel_detail.ImpossibleTravelDetail"
    ]
    """<p>Identifies unusual and impossible user activity for an account. </p>"""
    flagged_ip_address_detail: NotRequired[
        "aws_sdk_detective.types.flagged_ip_address_detail.FlaggedIpAddressDetail"
    ]
    """<p>Suspicious IP addresses that are flagged, which indicates critical or severe threats based on threat intelligence by Detective. This indicator is derived from Amazon Web Services threat intelligence.</p>"""
    new_geolocation_detail: NotRequired[
        "aws_sdk_detective.types.new_geolocation_detail.NewGeolocationDetail"
    ]
    """<p>Contains details about the new geographic location.</p>"""
    new_aso_detail: NotRequired["aws_sdk_detective.types.new_aso_detail.NewAsoDetail"]
    """<p>Contains details about the new Autonomous System Organization (ASO).</p>"""
    new_user_agent_detail: NotRequired[
        "aws_sdk_detective.types.new_user_agent_detail.NewUserAgentDetail"
    ]
    """<p>Contains details about the new user agent.</p>"""
    related_finding_detail: NotRequired[
        "aws_sdk_detective.types.related_finding_detail.RelatedFindingDetail"
    ]
    """<p>Contains details about related findings.</p>"""
    related_finding_group_detail: NotRequired[
        "aws_sdk_detective.types.related_finding_group_detail.RelatedFindingGroupDetail"
    ]
    """<p>Contains details about related finding groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndicatorDetail) -> dict:
    out: dict = {}
    if "tt_ps_observed_detail" in value:
        import aws_sdk_detective.types.tt_ps_observed_detail

        out["TTPsObservedDetail"] = (
            aws_sdk_detective.types.tt_ps_observed_detail.serialize_json(
                value["tt_ps_observed_detail"]
            )
        )
    if "impossible_travel_detail" in value:
        import aws_sdk_detective.types.impossible_travel_detail

        out["ImpossibleTravelDetail"] = (
            aws_sdk_detective.types.impossible_travel_detail.serialize_json(
                value["impossible_travel_detail"]
            )
        )
    if "flagged_ip_address_detail" in value:
        import aws_sdk_detective.types.flagged_ip_address_detail

        out["FlaggedIpAddressDetail"] = (
            aws_sdk_detective.types.flagged_ip_address_detail.serialize_json(
                value["flagged_ip_address_detail"]
            )
        )
    if "new_geolocation_detail" in value:
        import aws_sdk_detective.types.new_geolocation_detail

        out["NewGeolocationDetail"] = (
            aws_sdk_detective.types.new_geolocation_detail.serialize_json(
                value["new_geolocation_detail"]
            )
        )
    if "new_aso_detail" in value:
        import aws_sdk_detective.types.new_aso_detail

        out["NewAsoDetail"] = aws_sdk_detective.types.new_aso_detail.serialize_json(
            value["new_aso_detail"]
        )
    if "new_user_agent_detail" in value:
        import aws_sdk_detective.types.new_user_agent_detail

        out["NewUserAgentDetail"] = (
            aws_sdk_detective.types.new_user_agent_detail.serialize_json(
                value["new_user_agent_detail"]
            )
        )
    if "related_finding_detail" in value:
        import aws_sdk_detective.types.related_finding_detail

        out["RelatedFindingDetail"] = (
            aws_sdk_detective.types.related_finding_detail.serialize_json(
                value["related_finding_detail"]
            )
        )
    if "related_finding_group_detail" in value:
        import aws_sdk_detective.types.related_finding_group_detail

        out["RelatedFindingGroupDetail"] = (
            aws_sdk_detective.types.related_finding_group_detail.serialize_json(
                value["related_finding_group_detail"]
            )
        )
    return out


def deserialize_json(data: dict) -> IndicatorDetail:
    out: IndicatorDetail = {}  # type: ignore[typeddict-item]
    if "TTPsObservedDetail" in data:
        import aws_sdk_detective.types.tt_ps_observed_detail

        out["tt_ps_observed_detail"] = (
            aws_sdk_detective.types.tt_ps_observed_detail.deserialize_json(
                data["TTPsObservedDetail"]
            )
        )
    if "ImpossibleTravelDetail" in data:
        import aws_sdk_detective.types.impossible_travel_detail

        out["impossible_travel_detail"] = (
            aws_sdk_detective.types.impossible_travel_detail.deserialize_json(
                data["ImpossibleTravelDetail"]
            )
        )
    if "FlaggedIpAddressDetail" in data:
        import aws_sdk_detective.types.flagged_ip_address_detail

        out["flagged_ip_address_detail"] = (
            aws_sdk_detective.types.flagged_ip_address_detail.deserialize_json(
                data["FlaggedIpAddressDetail"]
            )
        )
    if "NewGeolocationDetail" in data:
        import aws_sdk_detective.types.new_geolocation_detail

        out["new_geolocation_detail"] = (
            aws_sdk_detective.types.new_geolocation_detail.deserialize_json(
                data["NewGeolocationDetail"]
            )
        )
    if "NewAsoDetail" in data:
        import aws_sdk_detective.types.new_aso_detail

        out["new_aso_detail"] = aws_sdk_detective.types.new_aso_detail.deserialize_json(
            data["NewAsoDetail"]
        )
    if "NewUserAgentDetail" in data:
        import aws_sdk_detective.types.new_user_agent_detail

        out["new_user_agent_detail"] = (
            aws_sdk_detective.types.new_user_agent_detail.deserialize_json(
                data["NewUserAgentDetail"]
            )
        )
    if "RelatedFindingDetail" in data:
        import aws_sdk_detective.types.related_finding_detail

        out["related_finding_detail"] = (
            aws_sdk_detective.types.related_finding_detail.deserialize_json(
                data["RelatedFindingDetail"]
            )
        )
    if "RelatedFindingGroupDetail" in data:
        import aws_sdk_detective.types.related_finding_group_detail

        out["related_finding_group_detail"] = (
            aws_sdk_detective.types.related_finding_group_detail.deserialize_json(
                data["RelatedFindingGroupDetail"]
            )
        )
    return out
