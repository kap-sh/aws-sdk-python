"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageOriginRestrictions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.allow_publish
    import aws_sdk_codeartifact.types.allow_upstream


class PackageOriginRestrictions(TypedDict, closed=True):
    publish: "aws_sdk_codeartifact.types.allow_publish.AllowPublish"
    """<p>The package origin configuration that determines if new versions of the package can be published directly to the repository.</p>"""
    upstream: "aws_sdk_codeartifact.types.allow_upstream.AllowUpstream"
    """<p>The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageOriginRestrictions) -> dict:
    out: dict = {}
    import aws_sdk_codeartifact.types.allow_publish

    out["publish"] = aws_sdk_codeartifact.types.allow_publish.serialize_json(
        value["publish"]
    )
    import aws_sdk_codeartifact.types.allow_upstream

    out["upstream"] = aws_sdk_codeartifact.types.allow_upstream.serialize_json(
        value["upstream"]
    )
    return out


def deserialize_json(data: dict) -> PackageOriginRestrictions:
    out: PackageOriginRestrictions = {}  # type: ignore[typeddict-item]
    if "publish" in data:
        import aws_sdk_codeartifact.types.allow_publish

        out["publish"] = aws_sdk_codeartifact.types.allow_publish.deserialize_json(
            data["publish"]
        )
    else:
        raise DeserializationError("PackageOriginRestrictions.publish required")
    if "upstream" in data:
        import aws_sdk_codeartifact.types.allow_upstream

        out["upstream"] = aws_sdk_codeartifact.types.allow_upstream.deserialize_json(
            data["upstream"]
        )
    else:
        raise DeserializationError("PackageOriginRestrictions.upstream required")
    return out
