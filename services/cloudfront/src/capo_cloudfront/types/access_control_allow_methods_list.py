"""Generated from Smithy shape ``com.amazonaws.cloudfront#AccessControlAllowMethodsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values

AccessControlAllowMethodsList: TypeAlias = list[
    "capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values.ResponseHeadersPolicyAccessControlAllowMethodsValues"
]


# --- restXml ser/de ---
def serialize_xml(
    value: AccessControlAllowMethodsList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values

        capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values.serialize_xml(
            item, el, "Method"
        )


def deserialize_xml(el: Element) -> AccessControlAllowMethodsList:
    import capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values

    out: AccessControlAllowMethodsList = []
    for child in el.findall("Method"):
        out.append(
            capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: AccessControlAllowMethodsList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values

        capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> AccessControlAllowMethodsList:
    import capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values

    out: AccessControlAllowMethodsList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.response_headers_policy_access_control_allow_methods_values.deserialize_xml(
                child
            )
        )
    return out
