"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.asset_bytes_type
    import aws_sdk_cognito_identity_provider.types.asset_category_type
    import aws_sdk_cognito_identity_provider.types.asset_extension_type
    import aws_sdk_cognito_identity_provider.types.color_scheme_mode_type
    import aws_sdk_cognito_identity_provider.types.resource_id_type


class AssetType(TypedDict):
    category: (
        "aws_sdk_cognito_identity_provider.types.asset_category_type.AssetCategoryType"
    )
    """<p>The category that the image corresponds to in your managed login configuration. Managed login has asset categories for different types of logos, backgrounds, and icons.</p>"""
    color_mode: "aws_sdk_cognito_identity_provider.types.color_scheme_mode_type.ColorSchemeModeType"
    """<p>The display-mode target of the asset: light, dark, or browser-adaptive. For example, Amazon Cognito displays a dark-mode image only when the browser or application is in dark mode, but displays a browser-adaptive file in all contexts.</p>"""
    extension: "aws_sdk_cognito_identity_provider.types.asset_extension_type.AssetExtensionType"
    """<p>The file type of the image file.</p>"""
    bytes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.asset_bytes_type.AssetBytesType"
    ]
    """<p>The image file, in Base64-encoded binary.</p>"""
    resource_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the asset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.asset_category_type

    out["Category"] = (
        aws_sdk_cognito_identity_provider.types.asset_category_type.serialize_aws_json_1_1(
            value["category"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.color_scheme_mode_type

    out["ColorMode"] = (
        aws_sdk_cognito_identity_provider.types.color_scheme_mode_type.serialize_aws_json_1_1(
            value["color_mode"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.asset_extension_type

    out["Extension"] = (
        aws_sdk_cognito_identity_provider.types.asset_extension_type.serialize_aws_json_1_1(
            value["extension"]
        )
    )
    if "bytes" in value:
        import aws_sdk_cognito_identity_provider.types.asset_bytes_type

        out["Bytes"] = (
            aws_sdk_cognito_identity_provider.types.asset_bytes_type.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetType:
    out: AssetType = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_cognito_identity_provider.types.asset_category_type

        out["category"] = (
            aws_sdk_cognito_identity_provider.types.asset_category_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    else:
        raise DeserializationError("AssetType.category required")
    if "ColorMode" in data:
        import aws_sdk_cognito_identity_provider.types.color_scheme_mode_type

        out["color_mode"] = (
            aws_sdk_cognito_identity_provider.types.color_scheme_mode_type.deserialize_aws_json_1_1(
                data["ColorMode"]
            )
        )
    else:
        raise DeserializationError("AssetType.color_mode required")
    if "Extension" in data:
        import aws_sdk_cognito_identity_provider.types.asset_extension_type

        out["extension"] = (
            aws_sdk_cognito_identity_provider.types.asset_extension_type.deserialize_aws_json_1_1(
                data["Extension"]
            )
        )
    else:
        raise DeserializationError("AssetType.extension required")
    if "Bytes" in data:
        import aws_sdk_cognito_identity_provider.types.asset_bytes_type

        out["bytes"] = (
            aws_sdk_cognito_identity_provider.types.asset_bytes_type.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out
