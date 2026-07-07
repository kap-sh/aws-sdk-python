"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.attributes_map
    import aws_sdk_iot.types.code_signing
    import aws_sdk_iot.types.file_location
    import aws_sdk_iot.types.file_name
    import aws_sdk_iot.types.file_type
    import aws_sdk_iot.types.ota_update_file_version


class OTAUpdateFile(TypedDict, closed=True):
    file_name: NotRequired["aws_sdk_iot.types.file_name.FileName"]
    """<p>The name of the file.</p>"""
    file_type: NotRequired["aws_sdk_iot.types.file_type.FileType"]
    """<p>An integer value you can include in the job document to allow your devices to identify the type of file received from the cloud.</p>"""
    file_version: NotRequired[
        "aws_sdk_iot.types.ota_update_file_version.OTAUpdateFileVersion"
    ]
    """<p>The file version.</p>"""
    file_location: NotRequired["aws_sdk_iot.types.file_location.FileLocation"]
    """<p>The location of the updated firmware.</p>"""
    code_signing: NotRequired["aws_sdk_iot.types.code_signing.CodeSigning"]
    """<p>The code signing method of the file.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.attributes_map.AttributesMap"]
    """<p>A list of name-attribute pairs. They won't be sent to devices as a part of the Job document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateFile) -> dict:
    out: dict = {}
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    if "file_type" in value:
        out["fileType"] = value["file_type"]
    if "file_version" in value:
        out["fileVersion"] = value["file_version"]
    if "file_location" in value:
        import aws_sdk_iot.types.file_location

        out["fileLocation"] = aws_sdk_iot.types.file_location.serialize_json(
            value["file_location"]
        )
    if "code_signing" in value:
        import aws_sdk_iot.types.code_signing

        out["codeSigning"] = aws_sdk_iot.types.code_signing.serialize_json(
            value["code_signing"]
        )
    if "attributes" in value:
        import aws_sdk_iot.types.attributes_map

        out["attributes"] = aws_sdk_iot.types.attributes_map.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> OTAUpdateFile:
    out: OTAUpdateFile = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    if "fileType" in data:
        out["file_type"] = data["fileType"]
    if "fileVersion" in data:
        out["file_version"] = data["fileVersion"]
    if "fileLocation" in data:
        import aws_sdk_iot.types.file_location

        out["file_location"] = aws_sdk_iot.types.file_location.deserialize_json(
            data["fileLocation"]
        )
    if "codeSigning" in data:
        import aws_sdk_iot.types.code_signing

        out["code_signing"] = aws_sdk_iot.types.code_signing.deserialize_json(
            data["codeSigning"]
        )
    if "attributes" in data:
        import aws_sdk_iot.types.attributes_map

        out["attributes"] = aws_sdk_iot.types.attributes_map.deserialize_json(
            data["attributes"]
        )
    return out
