"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ListenerAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_attribute_key
    import capo_elastic_load_balancing_v2.types.listener_attribute_value


class ListenerAttribute(TypedDict, closed=True):
    key: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_attribute_key.ListenerAttributeKey"
    ]
    """<p>The name of the attribute.</p> <p>The following attribute is supported by Network Load Balancers, and Gateway Load Balancers.</p> <ul> <li> <p> <code>tcp.idle_timeout.seconds</code> - The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.</p> </li> </ul> <p>The following attributes are only supported by Application Load Balancers.</p> <ul> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert_serial_number.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert-Serial-Number</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert_issuer.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert-Issuer</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert_subject.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert-Subject</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert_validity.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert-Validity</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert_leaf.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert-Leaf</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_mtls_clientcert.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Mtls-Clientcert</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_tls_version.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Tls-Version</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.request.x_amzn_tls_cipher_suite.header_name</code> - Enables you to modify the header name of the <b>X-Amzn-Tls-Cipher-Suite</b> HTTP request header.</p> </li> <li> <p> <code>routing.http.response.server.enabled</code> - Enables you to allow or remove the HTTP response server header.</p> </li> <li> <p> <code>routing.http.response.strict_transport_security.header_value</code> - Informs browsers that the site should only be accessed using HTTPS, and that any future attempts to access it using HTTP should automatically be converted to HTTPS.</p> </li> <li> <p> <code>routing.http.response.access_control_allow_origin.header_value</code> - Specifies which origins are allowed to access the server.</p> </li> <li> <p> <code>routing.http.response.access_control_allow_methods.header_value</code> - Returns which HTTP methods are allowed when accessing the server from a different origin.</p> </li> <li> <p> <code>routing.http.response.access_control_allow_headers.header_value</code> - Specifies which headers can be used during the request.</p> </li> <li> <p> <code>routing.http.response.access_control_allow_credentials.header_value</code> - Indicates whether the browser should include credentials such as cookies or authentication when making requests.</p> </li> <li> <p> <code>routing.http.response.access_control_expose_headers.header_value</code> - Returns which headers the browser can expose to the requesting client.</p> </li> <li> <p> <code>routing.http.response.access_control_max_age.header_value</code> - Specifies how long the results of a preflight request can be cached, in seconds.</p> </li> <li> <p> <code>routing.http.response.content_security_policy.header_value</code> - Specifies restrictions enforced by the browser to help minimize the risk of certain types of security threats.</p> </li> <li> <p> <code>routing.http.response.x_content_type_options.header_value</code> - Indicates whether the MIME types advertised in the <b>Content-Type</b> headers should be followed and not be changed.</p> </li> <li> <p> <code>routing.http.response.x_frame_options.header_value</code> - Indicates whether the browser is allowed to render a page in a <b>frame</b>, <b>iframe</b>, <b>embed</b> or <b>object</b>.</p> </li> </ul>"""
    value: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_attribute_value.ListenerAttributeValue"
    ]
    """<p>The value of the attribute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListenerAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> ListenerAttribute:
    out: ListenerAttribute = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
