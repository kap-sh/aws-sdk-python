"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AccountId``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
from aws_sdk_bcm_pricing_calculator._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccountId: TypeAlias = str