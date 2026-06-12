"""Generated from Smithy shape ``com.amazonaws.ecr#RegistryScanningRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.scan_frequency
    import aws_sdk_ecr.types.scanning_repository_filter_list


class RegistryScanningRule(TypedDict):
    scan_frequency: "aws_sdk_ecr.types.scan_frequency.ScanFrequency"
    """<p>The frequency that scans are performed at for a private registry. When the <code>ENHANCED</code> scan type is specified, the supported scan frequencies are <code>CONTINUOUS_SCAN</code> and <code>SCAN_ON_PUSH</code>. When the <code>BASIC</code> scan type is specified, the <code>SCAN_ON_PUSH</code> scan frequency is supported. If scan on push is not specified, then the <code>MANUAL</code> scan frequency is set by default.</p>"""
    repository_filters: (
        "aws_sdk_ecr.types.scanning_repository_filter_list.ScanningRepositoryFilterList"
    )
    """<p>The repository filters associated with the scanning configuration for a private registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryScanningRule) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.scan_frequency

    out["scanFrequency"] = aws_sdk_ecr.types.scan_frequency.serialize_aws_json_1_1(
        value["scan_frequency"]
    )
    import aws_sdk_ecr.types.scanning_repository_filter_list

    out["repositoryFilters"] = (
        aws_sdk_ecr.types.scanning_repository_filter_list.serialize_aws_json_1_1(
            value["repository_filters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryScanningRule:
    out: RegistryScanningRule = {}  # type: ignore[typeddict-item]
    if "scanFrequency" in data:
        import aws_sdk_ecr.types.scan_frequency

        out["scan_frequency"] = (
            aws_sdk_ecr.types.scan_frequency.deserialize_aws_json_1_1(
                data["scanFrequency"]
            )
        )
    else:
        raise DeserializationError("RegistryScanningRule.scan_frequency required")
    if "repositoryFilters" in data:
        import aws_sdk_ecr.types.scanning_repository_filter_list

        out["repository_filters"] = (
            aws_sdk_ecr.types.scanning_repository_filter_list.deserialize_aws_json_1_1(
                data["repositoryFilters"]
            )
        )
    else:
        raise DeserializationError("RegistryScanningRule.repository_filters required")
    return out
