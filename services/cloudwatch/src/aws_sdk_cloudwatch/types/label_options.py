"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.get_metric_data_label_timezone


class LabelOptions(TypedDict):
    timezone: NotRequired[
        "aws_sdk_cloudwatch.types.get_metric_data_label_timezone.GetMetricDataLabelTimezone"
    ]
    """<p>The time zone to use for metric data return in this operation. The format is <code>+</code> or <code>-</code> followed by four digits. The first two digits indicate the number of hours ahead or behind of UTC, and the final two digits are the number of minutes. For example, +0130 indicates a time zone that is 1 hour and 30 minutes ahead of UTC. The default is +0000. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelOptions) -> dict:
    out: dict = {}
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LabelOptions:
    out: LabelOptions = {}  # type: ignore[typeddict-item]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: LabelOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "timezone" in value:
        pairs.append((f"{prefix}.Timezone", str(value["timezone"])))


def deserialize_query(el: Element) -> LabelOptions:
    out: LabelOptions = {}  # type: ignore[typeddict-item]
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    return out
