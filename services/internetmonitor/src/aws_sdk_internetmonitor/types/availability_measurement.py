"""Generated from Smithy shape ``com.amazonaws.internetmonitor#AvailabilityMeasurement``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AvailabilityMeasurement(TypedDict):
    experience_score: NotRequired["float"]
    """<p>Experience scores, or health scores are calculated for different geographic and network provider combinations (that is, different granularities) and also summed into global scores. If you view performance or availability scores without filtering for any specific geography or service provider, Amazon CloudWatch Internet Monitor provides global health scores.</p> <p>The Amazon CloudWatch Internet Monitor chapter in the <i>CloudWatch User Guide</i> includes detailed information about how Internet Monitor calculates health scores, including performance and availability scores, and when it creates and resolves health events. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores\">How Amazon Web Services calculates performance and availability scores</a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    percent_of_total_traffic_impacted: NotRequired["float"]
    """<p>The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.</p> <p>For information about how Internet Monitor calculates impact, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html\">How Internet Monitor works</a> in the Amazon CloudWatch Internet Monitor section of the Amazon CloudWatch User Guide.</p>"""
    percent_of_client_location_impacted: NotRequired["float"]
    """<p>The percentage of impact caused by a health event for client location traffic globally.</p> <p>For information about how Internet Monitor calculates impact, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html\">Inside Internet Monitor</a> in the Amazon CloudWatch Internet Monitor section of the Amazon CloudWatch User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityMeasurement) -> dict:
    out: dict = {}
    if "experience_score" in value:
        out["ExperienceScore"] = value["experience_score"]
    if "percent_of_total_traffic_impacted" in value:
        out["PercentOfTotalTrafficImpacted"] = value[
            "percent_of_total_traffic_impacted"
        ]
    if "percent_of_client_location_impacted" in value:
        out["PercentOfClientLocationImpacted"] = value[
            "percent_of_client_location_impacted"
        ]
    return out


def deserialize_json(data: dict) -> AvailabilityMeasurement:
    out: AvailabilityMeasurement = {}  # type: ignore[typeddict-item]
    if "ExperienceScore" in data:
        out["experience_score"] = data["ExperienceScore"]
    if "PercentOfTotalTrafficImpacted" in data:
        out["percent_of_total_traffic_impacted"] = data["PercentOfTotalTrafficImpacted"]
    if "PercentOfClientLocationImpacted" in data:
        out["percent_of_client_location_impacted"] = data[
            "PercentOfClientLocationImpacted"
        ]
    return out
