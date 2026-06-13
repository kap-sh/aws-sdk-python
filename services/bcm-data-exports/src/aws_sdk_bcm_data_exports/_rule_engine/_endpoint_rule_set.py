from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    get_attr,
    interpolate,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        Endpoint: str | None = None,
        Region: str | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.Region = Region if Region is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://bcm-data-exports.us-iso-east-1.c2s.ic.gov",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "us-iso-east-1", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso-b", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://bcm-data-exports.us-isob-east-1.sc2s.sgov.gov",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "us-isob-east-1", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso-e", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://bcm-data-exports.eu-isoe-west-1.cloud.adc-e.uk",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "eu-isoe-west-1", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso-f", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://bcm-data-exports.us-isof-south-1.csp.hci.ic.gov",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingRegion": interpolate(
                                        "us-isof-south-1", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
            if p.UseFIPS is True:
                return Endpoint(
                    url=interpolate(
                        "https://bcm-data-exports-fips.{PartitionResult#implicitGlobalRegion}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={
                        "authSchemes": [
                            {
                                "name": interpolate("sigv4", p, _locals),
                                "signingRegion": interpolate(
                                    "{PartitionResult#implicitGlobalRegion}", p, _locals
                                ),
                            }
                        ]
                    },
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://bcm-data-exports.{PartitionResult#implicitGlobalRegion}.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={
                    "authSchemes": [
                        {
                            "name": interpolate("sigv4", p, _locals),
                            "signingRegion": interpolate(
                                "{PartitionResult#implicitGlobalRegion}", p, _locals
                            ),
                        }
                    ]
                },
                headers={},
            )
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
