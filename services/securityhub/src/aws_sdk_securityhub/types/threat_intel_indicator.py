"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.threat_intel_indicator_category
    import aws_sdk_securityhub.types.threat_intel_indicator_type


class ThreatIntelIndicator(TypedDict):
    type: NotRequired[
        "aws_sdk_securityhub.types.threat_intel_indicator_type.ThreatIntelIndicatorType"
    ]
    """<p>The type of threat intelligence indicator.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of a threat intelligence indicator.</p> <p>Length Constraints: Minimum of 1 length. Maximum of 512 length.</p>"""
    category: NotRequired[
        "aws_sdk_securityhub.types.threat_intel_indicator_category.ThreatIntelIndicatorCategory"
    ]
    """<p>The category of a threat intelligence indicator.</p>"""
    last_observed_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the most recent instance of a threat intelligence indicator was observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    source: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source of the threat intelligence indicator.</p> <p>Length Constraints: Minimum of 1 length. Maximum of 64 length.</p>"""
    source_url: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL to the page or site where you can get more information about the threat intelligence indicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelIndicator) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_securityhub.types.threat_intel_indicator_type

        out["Type"] = (
            aws_sdk_securityhub.types.threat_intel_indicator_type.serialize_json(
                value["type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    if "category" in value:
        import aws_sdk_securityhub.types.threat_intel_indicator_category

        out["Category"] = (
            aws_sdk_securityhub.types.threat_intel_indicator_category.serialize_json(
                value["category"]
            )
        )
    if "last_observed_at" in value:
        out["LastObservedAt"] = value["last_observed_at"]
    if "source" in value:
        out["Source"] = value["source"]
    if "source_url" in value:
        out["SourceUrl"] = value["source_url"]
    return out


def deserialize_json(data: dict) -> ThreatIntelIndicator:
    out: ThreatIntelIndicator = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_securityhub.types.threat_intel_indicator_type

        out["type"] = (
            aws_sdk_securityhub.types.threat_intel_indicator_type.deserialize_json(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    if "Category" in data:
        import aws_sdk_securityhub.types.threat_intel_indicator_category

        out["category"] = (
            aws_sdk_securityhub.types.threat_intel_indicator_category.deserialize_json(
                data["Category"]
            )
        )
    if "LastObservedAt" in data:
        out["last_observed_at"] = data["LastObservedAt"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "SourceUrl" in data:
        out["source_url"] = data["SourceUrl"]
    return out
