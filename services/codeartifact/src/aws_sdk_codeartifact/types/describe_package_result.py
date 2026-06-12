"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_description


class DescribePackageResult(TypedDict):
    package: "aws_sdk_codeartifact.types.package_description.PackageDescription"
    """<p>A <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains information about the requested package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageResult) -> dict:
    out: dict = {}
    import aws_sdk_codeartifact.types.package_description

    out["package"] = aws_sdk_codeartifact.types.package_description.serialize_json(
        value["package"]
    )
    return out


def deserialize_json(data: dict) -> DescribePackageResult:
    out: DescribePackageResult = {}  # type: ignore[typeddict-item]
    if "package" in data:
        import aws_sdk_codeartifact.types.package_description

        out["package"] = (
            aws_sdk_codeartifact.types.package_description.deserialize_json(
                data["package"]
            )
        )
    else:
        raise DeserializationError("DescribePackageResult.package required")
    return out
