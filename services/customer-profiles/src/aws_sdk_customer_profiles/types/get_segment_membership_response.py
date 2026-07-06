"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.failures
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.profiles
    import aws_sdk_customer_profiles.types.timestamp


class GetSegmentMembershipResponse(TypedDict, closed=True):
    segment_definition_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The unique name of the segment definition.</p>"""
    profiles: NotRequired["aws_sdk_customer_profiles.types.profiles.Profiles"]
    """<p>An array of maps where each contains a response per profile requested.</p>"""
    failures: NotRequired["aws_sdk_customer_profiles.types.failures.Failures"]
    """<p>An array of maps where each contains a response per profile failed for the request.</p>"""
    last_computed_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp indicating when the segment membership was last computed or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentMembershipResponse) -> dict:
    out: dict = {}
    if "segment_definition_name" in value:
        out["SegmentDefinitionName"] = value["segment_definition_name"]
    if "profiles" in value:
        import aws_sdk_customer_profiles.types.profiles

        out["Profiles"] = aws_sdk_customer_profiles.types.profiles.serialize_json(
            value["profiles"]
        )
    if "failures" in value:
        import aws_sdk_customer_profiles.types.failures

        out["Failures"] = aws_sdk_customer_profiles.types.failures.serialize_json(
            value["failures"]
        )
    if "last_computed_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastComputedAt"] = (
            aws_sdk_customer_profiles.types.timestamp.serialize_json(
                value["last_computed_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSegmentMembershipResponse:
    out: GetSegmentMembershipResponse = {}  # type: ignore[typeddict-item]
    if "SegmentDefinitionName" in data:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    if "Profiles" in data:
        import aws_sdk_customer_profiles.types.profiles

        out["profiles"] = aws_sdk_customer_profiles.types.profiles.deserialize_json(
            data["Profiles"]
        )
    if "Failures" in data:
        import aws_sdk_customer_profiles.types.failures

        out["failures"] = aws_sdk_customer_profiles.types.failures.deserialize_json(
            data["Failures"]
        )
    if "LastComputedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_computed_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastComputedAt"]
            )
        )
    return out
