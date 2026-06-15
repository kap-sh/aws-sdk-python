"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.custom_object_identifier
    import aws_sdk_acm_pca.types.extended_key_usage_type


class ExtendedKeyUsage(TypedDict):
    extended_key_usage_type: NotRequired[
        "aws_sdk_acm_pca.types.extended_key_usage_type.ExtendedKeyUsageType"
    ]
    r"""<p>Specifies a standard <code>ExtendedKeyUsage</code> as defined as in <a href=\"https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12\">RFC 5280</a>.</p>"""
    extended_key_usage_object_identifier: NotRequired[
        "aws_sdk_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    ]
    """<p>Specifies a custom <code>ExtendedKeyUsage</code> with an object identifier (OID).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsage) -> dict:
    out: dict = {}
    if "extended_key_usage_type" in value:
        import aws_sdk_acm_pca.types.extended_key_usage_type

        out["ExtendedKeyUsageType"] = (
            aws_sdk_acm_pca.types.extended_key_usage_type.serialize_aws_json_1_1(
                value["extended_key_usage_type"]
            )
        )
    if "extended_key_usage_object_identifier" in value:
        out["ExtendedKeyUsageObjectIdentifier"] = value[
            "extended_key_usage_object_identifier"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendedKeyUsage:
    out: ExtendedKeyUsage = {}  # type: ignore[typeddict-item]
    if "ExtendedKeyUsageType" in data:
        import aws_sdk_acm_pca.types.extended_key_usage_type

        out["extended_key_usage_type"] = (
            aws_sdk_acm_pca.types.extended_key_usage_type.deserialize_aws_json_1_1(
                data["ExtendedKeyUsageType"]
            )
        )
    if "ExtendedKeyUsageObjectIdentifier" in data:
        out["extended_key_usage_object_identifier"] = data[
            "ExtendedKeyUsageObjectIdentifier"
        ]
    return out
