"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#FixedResponseActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.fixed_response_action_content_type
    import capo_elastic_load_balancing_v2.types.fixed_response_action_message
    import capo_elastic_load_balancing_v2.types.fixed_response_action_status_code


class FixedResponseActionConfig(TypedDict, closed=True):
    message_body: NotRequired[
        "capo_elastic_load_balancing_v2.types.fixed_response_action_message.FixedResponseActionMessage"
    ]
    """<p>The message.</p>"""
    status_code: NotRequired[
        "capo_elastic_load_balancing_v2.types.fixed_response_action_status_code.FixedResponseActionStatusCode"
    ]
    """<p>The HTTP response code (2XX, 4XX, or 5XX).</p>"""
    content_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.fixed_response_action_content_type.FixedResponseActionContentType"
    ]
    """<p>The content type.</p> <p>Valid Values: text/plain | text/css | text/html | application/javascript | application/json</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FixedResponseActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message_body" in value:
        pairs.append((f"{key_prefix}MessageBody", str(value["message_body"])))
    if "status_code" in value:
        pairs.append((f"{key_prefix}StatusCode", str(value["status_code"])))
    if "content_type" in value:
        pairs.append((f"{key_prefix}ContentType", str(value["content_type"])))


def deserialize_query(el: Element) -> FixedResponseActionConfig:
    out: FixedResponseActionConfig = {}  # type: ignore[typeddict-item]
    child_message_body = el.find("MessageBody")
    if child_message_body is not None:
        out["message_body"] = str(child_message_body.text or "")
    child_status_code = el.find("StatusCode")
    if child_status_code is not None:
        out["status_code"] = str(child_status_code.text or "")
    child_content_type = el.find("ContentType")
    if child_content_type is not None:
        out["content_type"] = str(child_content_type.text or "")
    return out
