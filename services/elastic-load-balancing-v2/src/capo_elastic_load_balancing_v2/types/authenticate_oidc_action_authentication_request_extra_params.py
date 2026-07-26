"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AuthenticateOidcActionAuthenticationRequestExtraParams``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_param_name
    import capo_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_param_value

AuthenticateOidcActionAuthenticationRequestExtraParams: TypeAlias = dict[
    "capo_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_param_name.AuthenticateOidcActionAuthenticationRequestParamName",
    "capo_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_param_value.AuthenticateOidcActionAuthenticationRequestParamValue",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: AuthenticateOidcActionAuthenticationRequestExtraParams,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        pairs.append((f"{prefix}.entry.{n}.value", str(value)))


def deserialize_query(
    el: Element,
) -> AuthenticateOidcActionAuthenticationRequestExtraParams:
    out: AuthenticateOidcActionAuthenticationRequestExtraParams = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: AuthenticateOidcActionAuthenticationRequestExtraParams,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        pairs.append((f"{prefix}.{n}.value", str(value)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> AuthenticateOidcActionAuthenticationRequestExtraParams:
    out: AuthenticateOidcActionAuthenticationRequestExtraParams = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
