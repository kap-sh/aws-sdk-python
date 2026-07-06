"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AdditionalAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.additional_attribute_key
    import aws_sdk_elastic_load_balancing.types.additional_attribute_value


class AdditionalAttribute(TypedDict, closed=True):
    key: NotRequired[
        "aws_sdk_elastic_load_balancing.types.additional_attribute_key.AdditionalAttributeKey"
    ]
    """<p>The name of the attribute.</p> <p>The following attribute is supported.</p> <ul> <li> <p> <code>elb.http.desyncmitigationmode</code> - Determines how the load balancer handles requests that might pose a security risk to your application. The possible values are <code>monitor</code>, <code>defensive</code>, and <code>strictest</code>. The default is <code>defensive</code>.</p> </li> </ul>"""
    value: NotRequired[
        "aws_sdk_elastic_load_balancing.types.additional_attribute_value.AdditionalAttributeValue"
    ]
    """<p>This value of the attribute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AdditionalAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> AdditionalAttribute:
    out: AdditionalAttribute = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
