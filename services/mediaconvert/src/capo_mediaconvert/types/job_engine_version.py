"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobEngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__timestamp_unix


class JobEngineVersion(TypedDict, closed=True):
    expiration_date: NotRequired[
        "capo_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The date that this Job engine version expires. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested."""
    version: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions represent periodically grouped MediaConvert releases with new features, updates, improvements, and fixes. Job engine versions are in a YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support."""


# --- restJson1 ser/de ---
def serialize_json(value: JobEngineVersion) -> dict:
    out: dict = {}
    if "expiration_date" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["expirationDate"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["expiration_date"]
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> JobEngineVersion:
    out: JobEngineVersion = {}  # type: ignore[typeddict-item]
    if "expirationDate" in data:
        import capo_mediaconvert.types.__timestamp_unix

        out["expiration_date"] = (
            capo_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["expirationDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
