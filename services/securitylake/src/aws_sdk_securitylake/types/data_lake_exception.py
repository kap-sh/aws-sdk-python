"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securitylake.types.region
    import aws_sdk_securitylake.types.safe_string


class DataLakeException(TypedDict, closed=True):
    region: NotRequired["aws_sdk_securitylake.types.region.Region"]
    """<p>The Amazon Web Services Regions where the exception occurred.</p>"""
    exception: NotRequired["aws_sdk_securitylake.types.safe_string.SafeString"]
    """<p>The underlying exception of a Security Lake exception.</p>"""
    remediation: NotRequired["aws_sdk_securitylake.types.safe_string.SafeString"]
    """<p>List of all remediation steps for a Security Lake exception.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>This error can occur if you configure the wrong timestamp format, or if the subset of entries used for validation had errors or missing values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeException) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "exception" in value:
        out["exception"] = value["exception"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "timestamp" in value:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["timestamp"] = aws_sdk_securitylake.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> DataLakeException:
    out: DataLakeException = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "exception" in data:
        out["exception"] = data["exception"]
    if "remediation" in data:
        out["remediation"] = data["remediation"]
    if "timestamp" in data:
        import aws_sdk_securitylake.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_securitylake.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    return out
