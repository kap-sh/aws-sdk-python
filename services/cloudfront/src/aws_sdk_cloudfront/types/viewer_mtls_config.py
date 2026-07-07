"""Generated from Smithy shape ``com.amazonaws.cloudfront#ViewerMtlsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.trust_store_config
    import aws_sdk_cloudfront.types.viewer_mtls_mode


class ViewerMtlsConfig(TypedDict, closed=True):
    mode: "aws_sdk_cloudfront.types.viewer_mtls_mode.ViewerMtlsMode"
    """<p>The viewer mTLS mode.</p>"""
    trust_store_config: NotRequired[
        "aws_sdk_cloudfront.types.trust_store_config.TrustStoreConfig"
    ]
    """<p>The trust store configuration associated with the viewer mTLS configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ViewerMtlsConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.viewer_mtls_mode

    aws_sdk_cloudfront.types.viewer_mtls_mode.serialize_xml(
        value.get("mode", "required"), el, "Mode"
    )
    if "trust_store_config" in value:
        import aws_sdk_cloudfront.types.trust_store_config

        aws_sdk_cloudfront.types.trust_store_config.serialize_xml(
            value["trust_store_config"], el, "TrustStoreConfig"
        )


def deserialize_xml(el: Element) -> ViewerMtlsConfig:
    out: ViewerMtlsConfig = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_cloudfront.types.viewer_mtls_mode

        out["mode"] = aws_sdk_cloudfront.types.viewer_mtls_mode.deserialize_xml(
            child_mode
        )
    else:
        out["mode"] = "required"
    child_trust_store_config = el.find("TrustStoreConfig")
    if child_trust_store_config is not None:
        import aws_sdk_cloudfront.types.trust_store_config

        out["trust_store_config"] = (
            aws_sdk_cloudfront.types.trust_store_config.deserialize_xml(
                child_trust_store_config
            )
        )
    return out
