"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_version_description


class DescribePackageVersionResult(TypedDict):
    package_version: "aws_sdk_codeartifact.types.package_version_description.PackageVersionDescription"
    r"""<p> A <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains information about the requested package version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionResult) -> dict:
    out: dict = {}
    import aws_sdk_codeartifact.types.package_version_description

    out["packageVersion"] = (
        aws_sdk_codeartifact.types.package_version_description.serialize_json(
            value["package_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribePackageVersionResult:
    out: DescribePackageVersionResult = {}  # type: ignore[typeddict-item]
    if "packageVersion" in data:
        import aws_sdk_codeartifact.types.package_version_description

        out["package_version"] = (
            aws_sdk_codeartifact.types.package_version_description.deserialize_json(
                data["packageVersion"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageVersionResult.package_version required"
        )
    return out
