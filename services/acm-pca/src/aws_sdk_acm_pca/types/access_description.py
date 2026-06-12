"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.access_method
    import aws_sdk_acm_pca.types.general_name


class AccessDescription(TypedDict):
    access_method: "aws_sdk_acm_pca.types.access_method.AccessMethod"
    """<p>The type and format of <code>AccessDescription</code> information.</p>"""
    access_location: "aws_sdk_acm_pca.types.general_name.GeneralName"
    """<p>The location of <code>AccessDescription</code> information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDescription) -> dict:
    out: dict = {}
    import aws_sdk_acm_pca.types.access_method

    out["AccessMethod"] = aws_sdk_acm_pca.types.access_method.serialize_aws_json_1_1(
        value["access_method"]
    )
    import aws_sdk_acm_pca.types.general_name

    out["AccessLocation"] = aws_sdk_acm_pca.types.general_name.serialize_aws_json_1_1(
        value["access_location"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDescription:
    out: AccessDescription = {}  # type: ignore[typeddict-item]
    if "AccessMethod" in data:
        import aws_sdk_acm_pca.types.access_method

        out["access_method"] = (
            aws_sdk_acm_pca.types.access_method.deserialize_aws_json_1_1(
                data["AccessMethod"]
            )
        )
    else:
        raise DeserializationError("AccessDescription.access_method required")
    if "AccessLocation" in data:
        import aws_sdk_acm_pca.types.general_name

        out["access_location"] = (
            aws_sdk_acm_pca.types.general_name.deserialize_aws_json_1_1(
                data["AccessLocation"]
            )
        )
    else:
        raise DeserializationError("AccessDescription.access_location required")
    return out
