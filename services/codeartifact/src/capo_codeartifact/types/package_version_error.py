"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.error_message
    import capo_codeartifact.types.package_version_error_code


class PackageVersionError(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_codeartifact.types.package_version_error_code.PackageVersionErrorCode"
    ]
    """<p> The error code associated with the error. Valid error codes are: </p> <ul> <li> <p> <code>ALREADY_EXISTS</code> </p> </li> <li> <p> <code>MISMATCHED_REVISION</code> </p> </li> <li> <p> <code>MISMATCHED_STATUS</code> </p> </li> <li> <p> <code>NOT_ALLOWED</code> </p> </li> <li> <p> <code>NOT_FOUND</code> </p> </li> <li> <p> <code>SKIPPED</code> </p> </li> </ul>"""
    error_message: NotRequired["capo_codeartifact.types.error_message.ErrorMessage"]
    """<p> The error message associated with the error. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_codeartifact.types.package_version_error_code

        out["errorCode"] = (
            capo_codeartifact.types.package_version_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> PackageVersionError:
    out: PackageVersionError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import capo_codeartifact.types.package_version_error_code

        out["error_code"] = (
            capo_codeartifact.types.package_version_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
