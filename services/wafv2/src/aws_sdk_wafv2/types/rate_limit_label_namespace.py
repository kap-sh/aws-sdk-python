"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitLabelNamespace``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.label_namespace


class RateLimitLabelNamespace(TypedDict, closed=True):
    namespace: "aws_sdk_wafv2.types.label_namespace.LabelNamespace"
    """<p>The namespace to use for aggregation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitLabelNamespace) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitLabelNamespace:
    out: RateLimitLabelNamespace = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("RateLimitLabelNamespace.namespace required")
    return out
