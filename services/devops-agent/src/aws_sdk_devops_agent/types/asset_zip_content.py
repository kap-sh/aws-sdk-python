"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetZipContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_zip_bytes


class AssetZipContent(TypedDict, closed=True):
    zip_file: "aws_sdk_devops_agent.types.asset_zip_bytes.AssetZipBytes"
    """<p>The zip file bytes</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetZipContent) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_zip_bytes

    out["zipFile"] = aws_sdk_devops_agent.types.asset_zip_bytes.serialize_json(
        value["zip_file"]
    )
    return out


def deserialize_json(data: dict) -> AssetZipContent:
    out: AssetZipContent = {}  # type: ignore[typeddict-item]
    if "zipFile" in data:
        import aws_sdk_devops_agent.types.asset_zip_bytes

        out["zip_file"] = aws_sdk_devops_agent.types.asset_zip_bytes.deserialize_json(
            data["zipFile"]
        )
    else:
        raise DeserializationError("AssetZipContent.zip_file required")
    return out
