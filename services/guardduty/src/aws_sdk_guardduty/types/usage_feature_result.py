"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeatureResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.total
    import aws_sdk_guardduty.types.usage_feature


class UsageFeatureResult(TypedDict):
    feature: NotRequired["aws_sdk_guardduty.types.usage_feature.UsageFeature"]
    """<p>The feature that generated the usage cost.</p>"""
    total: NotRequired["aws_sdk_guardduty.types.total.Total"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeatureResult) -> dict:
    out: dict = {}
    if "feature" in value:
        import aws_sdk_guardduty.types.usage_feature

        out["feature"] = aws_sdk_guardduty.types.usage_feature.serialize_json(
            value["feature"]
        )
    if "total" in value:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.serialize_json(value["total"])
    return out


def deserialize_json(data: dict) -> UsageFeatureResult:
    out: UsageFeatureResult = {}  # type: ignore[typeddict-item]
    if "feature" in data:
        import aws_sdk_guardduty.types.usage_feature

        out["feature"] = aws_sdk_guardduty.types.usage_feature.deserialize_json(
            data["feature"]
        )
    if "total" in data:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.deserialize_json(data["total"])
    return out
